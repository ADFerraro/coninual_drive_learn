import os
import time
import torch
import torch.nn as nn

torch.manual_seed(42)
img = torch.load('./input.pt', weights_only=True)
lab = torch.load('./label.pt', weights_only=True)
last_mod = os.stat('input.pt').st_mtime
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

model = torch.load('./policyNet.pt', weights_only=False)

criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
n_times = 0
out = model(img)
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

