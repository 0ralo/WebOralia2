from celery import Celery, shared_task
import os
import logging

logger = logging.getLogger(__file__)

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


@shared_task
def clean():
	files = os.listdir("media/codes/")
	for i in files:
		logger.info(i)
