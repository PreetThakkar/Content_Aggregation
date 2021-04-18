import subprocess

activate = "C:\\Users\\preet\\AppData\\Local\\Programs\\Python\\Python37\\Environments\\Djangoo\\Scripts\\activate.bat"
django = 'python manage.py runserver'
django_server = subprocess.Popen(f'cmd.exe /K {activate} && {django}')