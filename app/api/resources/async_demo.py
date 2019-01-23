from flask_restful import Resource
from app.tasks.example import dummy_task

class LongTask(Resource):
    def get(self):
        task = dummy_task.delay()
        ret = task.wait()
        return {"result": ret}