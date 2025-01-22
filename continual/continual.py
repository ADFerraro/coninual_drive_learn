import os
import time
import torch

img = torch.load('./img.pt')
last_mod = os.stat('test.txt').st_mtime

model = torch.load('./policyNet.pt', weights_only=False)

while os.stat('test.txt').st_mtime == last_mod:
    print('training..')
    time.sleep(5)
print('ending..')

