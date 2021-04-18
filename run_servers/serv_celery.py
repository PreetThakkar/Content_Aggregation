import subprocess

activate = "C:\\Users\\preet\\AppData\\Local\\Programs\\Python\\Python37\\Environments\\Djangoo\\Scripts\\activate.bat"
celery = 'celery -A Content_Aggregation worker -l info -P eventlet'
celery_server = subprocess.Popen(f'cmd.exe /K {activate} && {celery}')