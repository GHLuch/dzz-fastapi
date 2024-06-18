from collections import Counter
import os
import io
import uuid
import json
from botocore.parsers import json
from botocore.retryhandler import random
from botocore.session import get_session
from fastapi import FastAPI, HTTPException, UploadFile, File, APIRouter, Depends, status, WebSocket, WebSocketDisconnect, WebSocketException
from fastapi.responses import FileResponse, StreamingResponse, Response
from websockets.exceptions import ConnectionClosedError, ConnectionClosedOK
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models import ProcessTask
from app.services.database import get_db
from app.services.s3 import s3
from app.rabbit import rabbit_router
image_router = APIRouter(prefix="/image", tags=["user"])

translations = {
	"car": "Легковых автомобилей",
	"heavy equipment": "Спец. техники",
	"bus": "Автобусов",
	"truck": "Грузовиков",
	"train": "Поездов",
	"small ship": "Судов менее 20м",
	"medium ship": "Судов от 20 м до 50 м",
	"big ship": "Судов 50 м и более",
	"helicopter": "Вертолетов",
	"airplane": "Самолетов"
}

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[uuid.UUID, WebSocket] = {}

    async def connect(self, task_id: uuid.UUID, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[task_id] = websocket

    def disconnect(self, task_id: uuid.UUID):
        self.active_connections.pop(task_id)

    async def send_personal_message(self, message: dict, task_id: uuid.UUID):
        await self.active_connections[task_id].send_json(message)

manager = ConnectionManager()

UPLOAD_FOLDER = 'uploads'

@image_router.post("/upload")
async def upload_image(image: UploadFile = File(...), session: AsyncSession=Depends(get_db)):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    file_name = image.filename

    contents =  image.file.read()
    temp_file = io.BytesIO()
    temp_file.write(contents)
    temp_file.seek(0)
    task = ProcessTask(img_name=file_name)
    session.add(task)
    await session.commit()
    await session.refresh(task)
    s3.upload_fileobj(temp_file, "371b8969-dzz_super_heavy", f"{task.id}_{file_name}")
    temp_file.close()



    return {"message": f"Image {file_name} uploaded successfully", "task_id": task.id}

@image_router.post("/start_task/{task_id}")
async def start_task(task_id, session: AsyncSession = Depends(get_db)):
    query = select(ProcessTask).where(ProcessTask.id == task_id)
    task = (await session.execute(query)).scalar_one_or_none()
    if task is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "No task for this id")
    await rabbit_router.broker.publish(
        {"task_data": {"img_name": f"{task_id}_{task.img_name}", "task_id": task_id}},
        "tasks"
    )
    return {"message": "ok"}

@image_router.get("/result/{task_id}")
async def get_result_image(task_id):
    image = s3.get_object(Bucket='371b8969-dzz_super_heavy', Key=f"{task_id}_result.jpeg")
    image_file = image['Body'].read()
    return Response(image_file, media_type="image/jpeg")


@image_router.websocket("/status/{task_id}")
async def task_status(websocket: WebSocket, task_id: uuid.UUID):
    await manager.connect(task_id, websocket)
    try:
        while True:
            data = await websocket.receive()
            # await asyncio.sleep(3)
            # await manager.send_personal_message({"status": random.randint(1, 100)}, task_id)
    except (WebSocketDisconnect, WebSocketException, ConnectionClosedError, ConnectionClosedOK):
        manager.disconnect(task_id)

@rabbit_router.subscriber("task_status")
async def set_status(status_data: dict, session=Depends(get_db)):
    match status_data:
        case {"status": "process", "progress": progress, "task_id": task_id}:
            await manager.send_personal_message({"status": f"Обработка изображения: {progress}%", "stage": "process", "title_text": "В обработке..."}, uuid.UUID(task_id))
        case {"status": "finished", "found_objects": found_objects, "task_id": task_id}:
            found_objects = json.loads(found_objects)
            found_objects_names = [obj["name"] for obj in found_objects]
            found_objects_count = Counter(found_objects_names)
            found_objects_final = [{"name": translations.get(name, name), "count": found_objects_count[name]} for name in found_objects_count]
            query = select(ProcessTask).where(ProcessTask.id == task_id)
            task = (await session.execute(query)).scalar_one_or_none()
            task.completed = True
            await session.commit()
            await manager.send_personal_message({"status": "Обработка завершена!", "stage": "finished", "title_text": "Завершено", "found_objects": found_objects_final}, uuid.UUID(task_id))
