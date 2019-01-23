# flask-scalffold
based on miguelgrinberg/microblog and karec/cookiecutter-flask-restful


## Start celery worker
celery worker -A app.celery_app:celery_app --loglevel=info

## Todo
1. validate unit test and tox


## Attention
### celery 4.x imcompatible with windows 10 
[Unable to run tasks under Windows #4081](https://github.com/celery/celery/issues/4081)
1. pip install eventlet
2. $ celery worker -A app.celery_app:celery_app --loglevel=info -P eventlet

### celery4.2.0 imcompatible with ipython3.7.0
[Rename `async` to `asynchronous` (async is a reserved keyword in Python 3.7) #4879](https://github.com/celery/celery/pull/4879)
1. pip install --upgrade https://github.com/celery/celery/tarball/master
