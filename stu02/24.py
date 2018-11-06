import cv2
import numpy as np

def nothing(x):#回调函数
    pass

img = np.zeros((300,512,3), np.uint8)#300行,512列,3维,不包括刻度条
cv2.namedWindow('image')

cv2.createTrackbar('R','image',0,255,nothing)#创建刻度条
#五个参数分别为刻度条标签,窗口名,刻度默认值,刻度最大值,刻度变化时回调函数，该实例在窗口重绘时根据刻度值改变颜色，所以回调函数什么也不做
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar("switch", 'image',0,1,nothing)#当做按钮或者开关
print(len(img[0]))

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(1) == 27:
        break
    r = cv2.getTrackbarPos('R','image')# 获取刻度条值，两个参数分别为刻度条标签,窗口名
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos("switch",'image')

    if s == 0:
        img[:] = 0#按钮关时，显示背景色
    else:
        img[:] = [b,g,r]
cv2.destroyAllWindows()