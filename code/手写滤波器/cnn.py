#！ usr/bin/env python
# coding: utf-8

######## 自己创建一个二维卷积滤波器
import numpy as np
import cv2
import matplotlib.pyplot as plt
picpath = "../../PIC/lf.jpg"
img = cv2.imread(picpath,0)
kernal = np.zeros((10,10), np.float32)/100
print(kernal)
# 这里用numpy创建一个5*5的单位阵，ones表示这是单位阵，np.float32表示数据的格式是浮点32型。
# 最后单位阵的每个元素再除以25（5*5），整个滤波器表示对一个5*5的矩阵上的数进行平均求和。
index = 0
for i in range(0,5):
    for j in range (0,10):
        index =0.03;
        kernal[i][j]+=index
print(kernal)

dst = cv2.filter2D(img, -1, kernal)
# 用一个像素点周围及其本身在内的25个点的像素平均值代替其本身。
# 也就是以一个像素点为中心的边长为5的正方形区域内像素值的平均值代替原有像素值

titles = ['srcImg','convImg']
imgs = [img, dst]

# 画图进行展示
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(imgs[i],"gray")
    plt.title(titles[i])
plt.show()
#### 可从图中看出，卷积滤波的方式会弱化边缘，使得边缘不那么清晰。
#### 去噪可以理解为降低图像获取过程中的随机因素
# 从另一方面来讲，去噪使图像内一个局部区域的像素趋于相同