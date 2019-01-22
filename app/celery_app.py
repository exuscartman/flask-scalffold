from app import init_celery


celery_app = init_celery()
celery_app.conf.imports += ('app.tasks',)
