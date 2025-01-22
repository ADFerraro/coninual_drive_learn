import torch
import pandas as pd
import time
import numpy as np

data=pd.read_csv('./encodings.csv', sep=';', header=None).astype('float32')
columns = ['center','left','right','steering','throttle','reverse', 'speed']
labs=pd.read_csv('./driving_log.csv', sep=';', names=columns)

for idx in range(len(data)):
    array=data.iloc[idx].to_numpy()
    lab=np.array(labs.iloc[idx]['steering'].astype('float32'))
    tensor=torch.from_numpy(array)
    lab_tensor=torch.from_numpy(lab)
    torch.save(tensor, './input.pt')
    torch.save(lab_tensor,'./label.pt')
    print("done")
    time.sleep(1)
    
