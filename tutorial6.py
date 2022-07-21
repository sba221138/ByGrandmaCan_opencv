import cv2

img = cv2.imread('shape.jpg')
imgContour = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img, 150, 200)
# 偵測外輪廓 cv2.RETR_EXTERNAL 不壓縮輪廓點 CHAIN_APPROX_NONE
# contours: 輪廓 hierarchy: 階程
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    
    # 畫輪廓在新copy的圖上
    # cv2.drawContours(要畫上去的圖, 輪廓參數, 每個都畫選-1, 藍色(255,0,0),線的粗度)
    cv2.drawContours(imgContour, cnt, -1, (255,0,0),4)
    area = cv2.contourArea(cnt)
    if area > 500:
        # 輪廓面積
        # print(cv2.contourArea(cnt))
        # 輪廓邊長 
        # cv2.arcLength(輪廓圖, 輪廓是否邊長閉合)
        peri = cv2.arcLength(cnt, True)
        # 用多邊形近似輪廓 可以推徹多邊形的近似形狀 近似值越大 多邊形的編越多， 近似值越小多邊形的邊越少
        # cv2.approxPolyDP(要近似的輪廓圖, 近似值(輪廓邊長 * 0.02), 邊長是否閉合)
        vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
        # 頂點的數目
        corners = len(vertices)
        # 用一個方形把vertices包住 回傳左上x 左上y 寬 高
        x, y, w, h = cv2.boundingRect(vertices)
        cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0),4)
        if corners == 3:
            cv2.putText(imgContour, 'triangle', (x, y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255), 2)
        elif corners == 4:
            cv2.putText(imgContour, 'rectangle', (x, y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255), 2)
        elif corners == 5:
            cv2.putText(imgContour, 'pentagon', (x, y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255), 2)
        elif corners >= 6:
            cv2.putText(imgContour, 'circle', (x, y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255), 2)
cv2.imshow('img',img)
cv2.imshow('canny', canny)
cv2.imshow('imgContour',imgContour)
cv2.waitKey(0)