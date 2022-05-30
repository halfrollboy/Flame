from fastapi import APIRouter
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from ..models.pydantic.message import Message
import json
from ..db.kafka.config import (
    loop,
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_CONSUMER_GROUP,
    KAFKA_TOPIC,
)

router_kafka = APIRouter(
    prefix="/kafka",
    tags=["kafka"],
    # dependencies=[Depends(get_token_handler)],
    responses={404: {"employee": "Not found"}},
)


@router_kafka.post("/create_message")
async def send(message: Message):
    producer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    try:
        print(f"Sending mesage with value {message}")
        value_json = json.dumps(message.__dict__).encode("utf-8")
        await producer.send_and_wait(topic=KAFKA_TOPIC, value=value_json)
    finally:
        await producer.stop()


# @router_kafka.get("/consume")
async def consume():
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        loop=loop,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id=KAFKA_CONSUMER_GROUP,
    )
    await consumer.start()
    try:
        async for msg in consumer:
            print(f"Consumer msg: {msg}")
    finally:
        await consumer.stop()
