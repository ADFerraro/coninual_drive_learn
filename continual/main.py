import os
import subprocess

os.system("python3 generate_empty.py")
try:
    p=subprocess.Popen(['python3', 'simulator.py'])
except subprocess.CalledProcessError as e:
    print(f'Error running simulator: {e}')

try:
    while True:
        #os.system("python3 continual.py")
        p1=subprocess.run(['python3', 'continual.py'], check=True)
except KeyboardInterrupt:
    p.kill()
    p1.kill()
    os._exit()
