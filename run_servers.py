import os

os.system("start cmd /K .\\run_servers\\serv_redis.py")
os.system("start cmd /K .\\run_servers\\serv_celery.py")
os.system("start cmd /K .\\run_servers\\serv_django.py")
os.system("start cmd /K .\\run_servers\\run_tasks.py")
