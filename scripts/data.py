import os
from datetime import datetime
import sys
import time
import subprocess
import keyboard


IMAGE_NAME = "imx390_isp_1920_1080.ppm"
BOARD_IP = "192.168.0.20"
acc = 0
brake = 0
steer = 0
while True:
    try:
        print("getting...")
        date=datetime.now().strftime("%Y-%m-%d-%H.%M.%S.%f")
        print(f"a: {acc}")
        print(f"b: {brake}")
        print(f"s: {steer}")
        #p=subprocess.run(f"scp root@{BOARD_IP}:/home/root/frames/{IMAGE_NAME} ./images/img_{date}.ppm >/dev/null",shell=True)
        print(f"img_{date} saved")
    except KeyboardInterrupt:
        print("exiting")
        #p.kill()
        sys.exit()

time.sleep(0.5)

