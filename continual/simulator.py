import torch
import pandas as pd
import time
import numpy as np

SLEEP_SECS = 1.5

data=pd.read_csv('./encodings.csv', sep=';', header=None).astype('float32')
columns = ['center','left','right','steering','throttle','reverse', 'speed']
labs=pd.read_csv('./driving_log.csv', sep=';', names=columns)

for idx in range(len(data)):
    array=data.iloc[idx].to_numpy()
    lab=np.array(labs.iloc[idx]['steering'].astype('float32'))
    lab=np.expand_dims(lab, axis=0)
    tensor=torch.from_numpy(array)
    lab_tensor=torch.from_numpy(lab)
    torch.unsqueeze(lab_tensor, -1 )
    torch.save(tensor, './input.pt')
    torch.save(lab_tensor,'./label.pt')
    print(f"done for sample {idx}")
    time.sleep(SLEEP_SECS)
    
