import numpy as np
import cv2
def call_back_func(event,x,y,flags,param):
    #flags: Any relevant flags passed by OpenCV.一般为1表示正确
    #params: Any extra parameters supplied by OpenCV.传递的参数
    if event==cv2.EVENT_LBUTTONDOWN:
        #print(flags,param)
        cv2.circle(img,(x+71,y+71),100,(0,255,0),1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('hello4')
#cv2.setMouseCallback('hello4',call_back_func,['he'])
cv2.setMouseCallback('hello4',call_back_func)

while True:
    cv2.imshow("hello4",img)
    if cv2.waitKey(20)==27:#20ms刷新
        break
cv2.destroyAllWindows()