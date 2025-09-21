import os, time
from rq import Worker, Queue, Connection
import redis
from ..config import settings

redis_conn = redis.from_url(settings.redis_url)

if __name__ == "__main__":
    with Connection(redis_conn):
        worker = Worker(map(Queue, ["default","plans"]))
        worker.work(with_scheduler=True)
