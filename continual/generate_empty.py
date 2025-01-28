import torch
import torch.nn as nn

PATH = "./policyNet.pt"

torch.manual_seed(42)

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

policyNet = PolicyNet()

torch.save(policyNet, PATH)
print("non trained model generated.")
