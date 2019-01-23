from app.extensions import celery
import time


@celery.task
def dummy_task():
    time.sleep(2)
    return "OK"
