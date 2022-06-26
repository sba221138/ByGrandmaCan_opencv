import cv2
import numpy as np

# kernel = np.ones((5, 5), np.uint8)
# kernel1 = np.ones((5, 5), np.uint8)

# img = cv2.imread('colorcolor.jpg')
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(img, (15, 15), 10)
# canny = cv2.Canny(img, 200, 250)
# dilate = cv2.dilate(canny, kernel, iterations=1)
# erode = cv2.erode(dilate, kernel1, iterations=1)


# # cv2.imshow('img', img)
# # cv2.imshow('gray', gray)
# # cv2.imshow('blur', blur)
# cv2.imshow('canny', canny)
# cv2.imshow('dilate', dilate)
# cv2.imshow('erode', erode)
# cv2.waitKey(0)

img = cv2.imread('colorcolor.jpg')
img = cv2.resize(img, (0,0), fx = 0.5,fy = 0.5)
# 彩色轉換成灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 高斯模糊 cv2.GaussianBlur(img, (kernal奇數, kernal奇數), 標準差)
blur = cv2.GaussianBlur(img, (15, 15), 10)

# 邊緣 cv2.Canny(img, 最低門檻值, 最高門檻值)
canny = cv2.Canny(img, 200, 250)


kernal = np.ones((10, 10), np.uint8)
# 膨脹  cv2.dilate(img, kernal, iterations = 膨脹次數)
dileate = cv2.dilate(canny, kernal, iterations = 1)

kernal_erode = np.ones((10, 10), np.uint8)
# 侵蝕
erode = cv2.erode(dileate, kernal_erode, iterations = 1)

# cv2.imshow('img',img)
# cv2.imshow('gray', gray)
# cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dileate', dileate)
cv2.imshow('erode', erode)
cv2.waitKey(0)