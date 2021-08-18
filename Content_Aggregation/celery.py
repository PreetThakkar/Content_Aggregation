import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Content_Aggregation.settings')

app = Celery('Content_Aggregation')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    #Scheduler Name
    'fetch_the_news': {
        'task': 'fetch_news', # Task Name (Name Specified in Decorator)
        'schedule': 300,
    },
}  