import os
import pandas as pd
import numpy as np
import math
import glob,os

# 讀取所有xlsx文件
path = r"D:\ps\NA04" # 這裡替換為你的xlsx文件的路徑
file = glob.glob(os.path.join(path,"*.csv"))
dl = []
for f in file:
    dl.append(pd.read_csv(f,header=2,usecols=["coords","x", "y"]))

print(dl)
# 合併所有數據
all_data = pd.concat(dl, ignore_index=True)

# 設定閾值
threshold = 0.1 # 這個閾值需要你根據實際情況設置，也就是動物在水中由於水的流動而產生的輕微浮動

# 計算動物的移動距離並判斷是否超過閾值
moving_periods = []
is_moving = False
for i in range(len(all_data) - 15):
    dx = all_data.iloc[i+15]['x'] - all_data.iloc[i]['x']
    dy = all_data.iloc[i+15]['y'] - all_data.iloc[i]['y']
    distance = np.sqrt(dx**2 + dy**2)
    
    if distance > threshold and not is_moving: # 開始移動
        is_moving = True
        start_time = i / 15
    elif distance <= threshold and is_moving: # 停止移動
        is_moving = False
        end_time = i / 15
        moving_periods.append((start_time, end_time))

# 如果動物在最後一個數據點仍在移動，我們需要把這段時間也計算在內
if is_moving:
    moving_periods.append((start_time, len(all_data) / 15))

# 計算總的移動時間
total_moving_time = sum(end - start for start, end in moving_periods)

print(f"動物的移動時間為 {total_moving_time} 秒")
