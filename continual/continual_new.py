import os
import time
import torch
import torch.nn as nn
import sys
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

print("reading data...")

torch.manual_seed(42)
data=pd.read_csv('./encodings.csv', sep=';', header=None).astype('float32')

columns = ['center','left','right','steering','throttle','reverse', 'speed']
labs=pd.read_csv('./driving_log.csv', sep=';', names=columns)

print("defining model...")

class PolicyNet(nn.Module):
    def __init__(self):
        super(PolicyNet, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(100, 300),
            nn.ReLU(),
            nn.Linear(300, 200),
            nn.ReLU(),
            nn.Linear(200, 100),
            nn.ReLU(),
            nn.Linear(100, 50),
            nn.ReLU(),
            nn.Linear(50, 1),
            nn.Tanh()
        )

    def forward(self, x):
        x = self.net(x)
        return x

model = PolicyNet()
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.0001)

print("starting training...")

n_times = 0
losses = []

for idx in range(len(data)):
    array = data.iloc[idx].to_numpy()
    lab=np.array(labs.iloc[idx]['steering'].astype('float32'))
    lab=np.expand_dims(lab, axis=0)
    input_t = torch.from_numpy(array)
    lab_t = torch.from_numpy(lab)
    torch.unsqueeze(lab_t, -1 )
    optimizer.zero_grad()
    out = model(input_t)
    loss = criterion(out, lab_t)
    loss.backward()
    optimizer.step()
    losses.append(loss.item())
    n_times = n_times + 1
    if(n_times % int(len(data) * 0.1))==0:
        print(f"train: {n_times // (int(len(data) * 0.1))}0% completed")

print("plotting training loss")
plt.plot(losses)
plt.ylabel('losses')
plt.show()
