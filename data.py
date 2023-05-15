import csv
import pandas as pd
import numpy as np
import math


#計算兩點坐標距離
def picdata(p1x,p1y,p2x,p2y):
    picp1 = np.array([p1x,p1y])
    picp2 = np.array([p2x,p2y])
    picp3 = picp1 - picp2
    picp4 = math.hypot(picp3[0],picp3[1])
    # picp5=round(picp4)
    picdis = str(picp4)
    print("兩點坐標的距離為"+picdis)



# 使用下面兩行程式碼就好


picdata(p1x=180,
        p1y=202,
        p2x=190,
        p2y=254)#輸入圖片2點坐標，如果啥都沒有就不用動


