import os
import pandas as pd
import numpy as np
import math
import glob,os

# 讀取所有xlsx文件
time = 15 #!視頻時間（分鐘）
fluidspeed = 45 #!速度閾值
sec = 30 #!幀數
path = r"D:\ps\NA04" # 這裡替換為你的xlsx文件的路徑
file = glob.glob(os.path.join(path,"*.csv"))
dl = []
for f in file:
    dl.append(pd.read_csv(f,header=2,usecols=["coords","x", "y"]))

for d in range(len(dl)):
    data1 = dl[d]
    id = data1['coords']
    x = data1['x']
    y = data1['y']
    MovingTime = 0
    is_moving = False
    for i in range(len(id) - 30):
        for j in range(30):#!這邊是判定一秒的總移動距離
            j1 = i+j
            distance_sec = 0
            plot1 = np.array([x[i],y[i]])
            plot2 = np.array([x[j1+1],y[j1+1]])
            distance = np.linalg.norm(plot1-plot2)
            distance_sec = distance + distance_sec
        #!以下是判斷這一秒移動距離有沒有超過閾值
        if distance_sec > fluidspeed and not is_moving: # 開始移動
            is_moving = True
            start_time = i
        elif distance_sec <= fluidspeed and is_moving: # 停止移動
            is_moving = False
            end_time = i 
            MovingTime_sec = (end_time - start_time)/30
            MovingTime = MovingTime + MovingTime_sec
    # 如果動物在最後一個數據點仍在移動，我們需要把這段時間也計算在內
    if is_moving:
        MovingTime_sec = (len(id)-start_time)/30
        MovingTime = MovingTime + MovingTime_sec
    ImortalTime = (time * 60) - MovingTime 
    print(file[d]+"的靜止是時間為*"+str(ImortalTime)+"sec")


