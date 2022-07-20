import cv2
import numpy as np
def empty(v):
    pass

img = cv2.imread('XiWinnie.jpg')
img = cv2.resize(img, (0,0),fx=0.5,fy=0.5)

# 我們創建TrackBar 手動動態查找顏色的色調、飽和度、亮度
cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar', 640, 320)

cv2.createTrackbar('Hue Min', 'TrackBar', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('Val Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBar', 255, 255, empty)

# HSV 跟RGB 一樣是表達顏色的意思而HSV更容易過濾顏色，Hue: 色調 Saturation: 飽和度 Value: 亮度
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while True:
    # 顯示TrackBar的值
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBar')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBar')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBar')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBar')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBar')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBar')
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    # 透過控制條的改變過濾顏色的動作

    # lower 和 upper 都是需要透過array 表示
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)
    # 將兩張圖片的bit比較計算當兩張照片都是1的時候得到結果才會是1，就可以過濾出我們要的顏色
    result = cv2.bitwise_and(img, img, mask=mask)
    
    cv2.imshow('img',img)
    cv2.imshow('hsv',hsv)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)
    cv2.waitKey(1)
