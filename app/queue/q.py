from redis import Redis
from rq import Queue

redis_connection = Redis(
    host="valkey",
    port="6379"
)

q = Queue(connection=redis_connection)
