import cv2
import numpy as np

drawing = False #是否在画
ix,iy = -1,-1#临时坐标，记录位置

def draw_lines(event,x,y,flags,param):
    global ix,iy,drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y#开始画的坐标
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(img,(ix,iy),(x,y),(0,255,0),1)#红色
            ix,iy=x,y#1111处
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

img = np.zeros((300,300,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_lines)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(1) == 27:#esc退出
        break

cv2.destroyAllWindows()