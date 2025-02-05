import os
from datetime import datetime
import sys
import time
import subprocess
#import keyboard
import json
#from PIL import Image
import shutil
import warnings
import argparse

parser = argparse.ArgumentParser(description="Collect a set of samples from the board")
parser.add_argument(
    "-n",
    "--samples-number",
    default=None,
    type=int,
    help="only record the given number of samples, with a FIFO policy",
)

args = parser.parse_args()
warnings.filterwarnings("ignore", message=".*UNC paths are not supported.*")
acc = 0
brake = 0
steer = 50

def on_w():
    global acc
    if(acc < 100):
        acc += 0.5

def on_s():
    global brake
    #if(brake <= 100):
    brake += 1
    if(brake > 100): brake=100

def on_w_release():
    global acc
    if(acc >= 0):
        acc -=1

def on_s_release():
    global brake
    #if(brake >= 0):
    brake -= 10
    if(brake<0):brake=0

IMAGE_NAME = "imx390_isp_1920_1080.ppm"
BOARD_IP = "192.168.0.20"
counter=0
queue=[]

date=datetime.now().strftime("%Y-%m-%d-%H.%M.%S.%f")
#keyboard.on_press_key("w", lambda _: on_w())
#keyboard.on_press_key("s", lambda _: on_s())

with open(os.path.abspath("..\..\log.json"), "w") as f:
    json.dump([],f)
shutil.rmtree(os.path.abspath(f"..\..\images"))
os.mkdir(os.path.abspath(f"..\..\images"))

while True:

    if(not keyboard.is_pressed('w')):
        acc -= 5
        if(acc < 0):
            acc = 0
    if(not keyboard.is_pressed('s')):
        brake -= 30
        if(brake < 0):
            brake = 0

    print(f"a:{acc}")
    print(f"b:{brake}")
    try:
        date=datetime.now().strftime("%Y-%m-%d-%H.%M.%S.%f")
        p=subprocess.run(f"scp root@{BOARD_IP}:/home/root/frames/{IMAGE_NAME} "+os.path.abspath(f"..\..\images\img_{date}.ppm"),shell=True)
        Image.open(os.path.abspath(f"..\..\images\img_{date}.ppm")).save(os.path.abspath(f"..\..\images\img_{date}.png"),"PNG")
        
        os.remove(os.path.abspath(f"..\..\images\img_{date}.ppm"))
        queue.append(f"img_{date}.png")
        # Shift images if the maximum number is reached
        if(args.samples_number and (counter >= args.samples_number)):
            os.remove(os.path.abspath(f"..\..\images\\"+queue[0]))
            queue.pop(0)
        
        #Create (png name+acc+brake+steer) dict and append it to the json
        with open(os.path.abspath("..\..\log.json"), "r") as f:
            data=json.load(f)

        data.append({"img": f"img_{date}.png", "throttle": acc, "brake": brake, "steering": steer})

        if(args.samples_number and (counter >= args.samples_number)):
            data.pop(0)

        with open(os.path.abspath("..\..\log.json"), "w") as f:
            json.dump(data,f, indent = 4)

            
        counter += 1        
        print(f"img_{date}.png saved")
    except KeyboardInterrupt:
        print("exiting")
        p.kill()
        sys.exit()

    time.sleep(0.5)
