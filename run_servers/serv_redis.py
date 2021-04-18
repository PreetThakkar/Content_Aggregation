import subprocess

activate = "C:\\Users\\preet\\AppData\\Local\\Programs\\Python\\Python37\\Environments\\Djangoo\\Scripts\\activate.bat"
redis = 'Redis-x64-3.0.504\\redis-server.exe'
redis_server = subprocess.Popen(f'cmd.exe /K {activate} && {redis}')