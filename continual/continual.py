import os
import time
import torch
import torch.nn as nn
import sys
import policy

if not os.path.isfile('input.pt'):
    sys.exit()

torch.manual_seed(42)
img = torch.load('./input.pt', weights_only=True)
lab = torch.load('./label.pt', weights_only=True)
last_mod = os.stat('input.pt').st_mtime
model = torch.load('./policyNet.pt', weights_only=False)

criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
n_times = 0
last = None
while os.stat('input.pt').st_mtime == last_mod:
    out = model(img)
    loss = criterion(out, lab)
    loss.backward()
    optimizer.step()
    n_times = n_times + 1
    last=loss.item()

print(f'n_times = {n_times}; last_loss {last}')
torch.save(model, './policyNet.pt')
print('ending..')

