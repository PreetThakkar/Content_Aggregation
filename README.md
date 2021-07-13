# Content_Aggregation

This project is based on Django framework and web scraping to gather information from various sources on a single platform.

Celery is a task queue/job queue based on distributed message passing. It is focused on real-time operation, but supports scheduling as well as in this project.
The tasks are executed concurrently on a single or more worker servers. In this project, I am executing the task asynchronously(in the background).

Celery Beat is a scheduler that announce tasks at regular intervals that will be executed by workers nodes in the cluster.

For this worker server RQ (Redis Queue) - a simple Python library for queuing jobs and processing them in the background with workers - is used. 

A worker is a Python process that typically runs in the background and exists solely as a work horse to perform lengthy or blocking tasks that you don’t want to perform inside web processes.

For the respective libraries, the following commands are to be initiated - 
- 'python manage.py runserver'
- 'celery -A Content_Aggregation beat -l info'
- 'Redis-x64-3.0.504\\redis-server.exe'
- 'celery -A Content_Aggregation worker -l info -P eventlet'
