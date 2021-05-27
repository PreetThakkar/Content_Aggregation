import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Content_Aggregation.settings')

app = Celery('Content_Aggregation')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    # #Scheduler Name
    # 'fetch_the_news': {
    #     # Task Name (Name Specified in Decorator)
    #     'task': 'fetch_news',  
    #     # Schedule      
    #     'schedule': 600,
    #     # Function Arguments 
    #     # 'args': ("Hello",) 
    # },
    'test_the_celery': {
        # Task Name (Name Specified in Decorator)
        'task': 'test_celery',  
        # Schedule      
        'schedule': 10,
        # Function Arguments 
        # 'args': ("Hello",) 
    }
}  