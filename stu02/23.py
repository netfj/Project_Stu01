import cv2
import numpy as np
import copy

drawing = False #是否在画
rectx,recty=-1,-1#矩形初始位置
imgtemp=0#原画纸

def draw_rects(event,x,y,flags,param):
    global drawing,rectx,recty,imgtemp,img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        imgtemp=copy.deepcopy(img)#深拷贝
        rectx,recty=x,y
        # print("LBUTTONDOWN")
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = copy.deepcopy(imgtemp)
            cv2.rectangle(img,(rectx,recty),(x,y),(0,255,0),1)#红色
            # print("MOUSEMOVE")

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

img = np.zeros((300,300,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_rects)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(1) == 27:#esc退出
        break

cv2.destroyAllWindows()