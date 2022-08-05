from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebOralia2.settings')

app = Celery("WebOralia2")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task
def add(x, y):
	return x + y


@app.task
def deleteimage(name):
	os.remove("media/codes/{}".format(name))
