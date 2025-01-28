import os
import subprocess

os.system("python3 generate_empty.py")
if os.path.isfile('input.pt'):
    os.remove('input.pt')
if os.path.isfile('label.pt'):
    os.remove('label.pt')

try:
    p=subprocess.Popen(['python3', 'simulator.py'])
except subprocess.CalledProcessError as e:
    print(f'Error running simulator: {e}')

try:
    while True:
        p1=subprocess.run(['python3', 'continual.py'], check=True)
except KeyboardInterrupt:
    p.kill()
    p1.kill()
    os._exit()
