import subprocess

activate = "C:\\Users\\preet\\AppData\\Local\\Programs\\Python\\Python37\\Environments\\Djangoo\\Scripts\\activate.bat"
celery_beat = 'celery -A Content_Aggregation beat -l info'
beat = subprocess.Popen(f'cmd.exe /K {activate} && {celery_beat}')