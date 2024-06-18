from faststream.rabbit.fastapi import RabbitRouter
from app.config import config

print(config.RABBIT_URL)
rabbit_router = RabbitRouter(config.RABBIT_URL)

