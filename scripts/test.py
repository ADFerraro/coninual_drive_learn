import time
from PIL import Image
from matplotlib import pyplot as plt

a = 0
b = 0
s = 50
sig_queue=[[],[],[]]
plt.ion()
fig, axs = plt.subplot_mosaic([['img', 'accel'],['img', 'brake'],['img', 'steer']],layout = 'constrained')
while True:
    a +=1

    image = Image.open("../../img/img_2025-02-04-11.24.34.868393.png")
    sig_queue[0].append(a)
    sig_queue[1].append(b)
    sig_queue[2].append(s)
    print(sig_queue[:][0])
    axs['img'].clear()
    axs['img'].set_title('image')
    axs['img'].imshow(image)

    
    axs['accel'].clear()
    axs['accel'].set_title('acceleration')
    axs['accel'].plot(sig_queue[0])
    
    axs['brake'].clear()
    axs['brake'].set_title('brake')
    axs['brake'].plot(sig_queue[1])

    axs['steer'].clear()
    axs['steer'].set_title('steer')
    axs['steer'].plot(sig_queue[2])
    
    plt.pause(0.01)
    if(len(sig_queue[0]) > 10):
        for q in sig_queue:
            q.pop(0)

    
    time.sleep(1)
