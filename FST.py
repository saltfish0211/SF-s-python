import os
import pandas as pd
import numpy as np
import math
import glob,os

# 第一步：讀取所有xlsx文件
path = r"D:\ps\NA04" # 這裡替換為你的xlsx文件的路徑
file = glob.glob(os.path.join(path,"*.csv"))

# 第二步：從每個文件中讀取數據並結合在一起


dl = []
for f in file:
    dl.append(pd.read_csv(f,header=2,usecols=["coords","x", "y"]))

print(dl)
# 第三步：計算動物的移動速度
dl['dx'] = dl['x'].diff() # diff()是對數據進行差分，也就是相鄰兩點的差值
dl['dy'] = dl['y'].diff()
dl['speed'] = np.sqrt(dl['dx']**2 + dl['dy']**2) * (1/15) # 這裡我們假定每15次id為實際時間1秒

# 第四步：判斷動物何時靜止和何時移動
threshold = 0.1 # 這個閾值需要你根據實際情況設置，也就是動物在水中由於水的流動而產生的輕微浮動
dl['is_moving'] = dl['speed'] > threshold

# 第五步：計算動物靜止移動的總時長
moving_time = dl['is_moving'].sum() * (1/15) # 這裡每15次id為實際時間1秒
total_time = len(dl) * (1/15)
still_time = total_time - moving_time

print(f"動物的移動時間為 {moving_time} 秒")
print(f"動物的靜止時間為 {still_time} 秒")
