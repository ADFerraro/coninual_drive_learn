import torch
import torch.nn as nn
import policy

PATH = "./policyNet.pt"

torch.manual_seed(42)
policyNet = policy.PolicyNet()

torch.save(policyNet, PATH)
print(policyNet)
print("non trained model generated.")
