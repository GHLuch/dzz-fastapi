from src.transport import rabbit_router
from src.service.s3 import s3
from PIL import Image, ImageDraw
from io import BytesIO
from ultralytics import YOLO
import cv2

model = YOLO("best.pt")


@rabbit_router.subscriber("tasks")
async def process_task(task_data):
    if task_data["img_name"] not in [file["Key"] for file in s3.list_objects(Bucket='371b8969-dzz_super_heavy')['Contents']]:
        print("error!")
        return "No such image on bucket"
    image_request = s3.get_object(Bucket='371b8969-dzz_super_heavy', Key=task_data["img_name"])
    await rabbit_router.broker.publish(
        {"status": "process", "progress": 50, "task_id": task_data["task_id"]},
        "task_status"
        )
    print(image_request)
    image_file = image_request['Body'].read()
    image = Image.open(BytesIO(image_file))
    results = model(image)
    # image_draw = ImageDraw.Draw(image)
    # shape = ((0, 00), (100, 100)) 
    # image_draw.rectangle(shape, outline ="red") 
    
    result = results[0].plot()
    is_success, buffer = cv2.imencode('.jpg', result)
    in_mem_file = BytesIO(buffer)
    in_mem_file.seek(0)
    s3.upload_fileobj(in_mem_file, "371b8969-dzz_super_heavy", f"{task_data['task_id']}_result.jpeg")
    await rabbit_router.broker.publish(
        {"status": "finished", "found_objects": results[0].tojson(), "task_id": task_data["task_id"]},
        "task_status"
        )
    
