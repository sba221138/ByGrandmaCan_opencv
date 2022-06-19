import cv2

# cap = cv2.VideoCapture(1)


# while True:
#     ret, frame = cap.read()
#     if ret:
#         frame = cv2.resize(frame, (0, 0), fx=1.2, fy=1.2)
#         cv2.imshow('video', frame)
#     else:
#         break
#     if cv2.waitKey(10) == ord('q'):
#         break

## 讀取圖片

# # imread(讀取的圖檔路徑)
# img = cv2.imread('colorcolor.jpg')

# # cv2.resize(圖片, (0,0), fx=長的倍數, fy=寬的倍數) 
# # img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# # cv2.resize(圖片, 改變的大小)
# img = cv2.resize(img, (300, 300))

# # imshow(標題, 讀取圖檔)
# cv2.imshow('img', img)

# # waitKey(毫秒) 1000毫秒 == 1秒 如果寫0等於 無限時間
# cv2.waitKey(2000)

## 讀取影片

# # cv2.VideoCapture(讀取的影片路徑)
# cap = cv2.VideoCapture('thumb.mp4')

# while True:
#     # cap.read() >> 會吐出兩個值: 是否有下偵(bool value)我們用ret做變數, 下一張的畫面我們用 frame做變數
#     ret , frame = cap.read()
#     frame = cv2.resize(frame, (0,0), fx=0.4, fy=0.4)
#     if ret:
#         cv2.imshow('video', frame)
#     else:
#         break
#     # waitkey 離開透過 ord() 還傳 'q' 的ASCII 的數值 讓 waitkey取的停止的參數
#     if cv2.waitKey(10) == ord('q'):
#         break

## 讀取視訊鏡頭

# cv2.VideoCapture(視訊盡頭的編號) ex: 如果是筆電自己本身內建的鏡頭就是編號0，外接的可能就是別的數字
cap = cv2.VideoCapture(0)

while True:
    # cap.read() >> 會吐出兩個值: 是否有下偵(bool value)我們用ret做變數, 下一張的畫面我們用 frame做變數
    ret , frame = cap.read()
    frame = cv2.resize(frame, (0,0), fx=1.2, fy=1.2)
    if ret:
        cv2.imshow('video', frame)
    else:
        break
    # waitkey 離開透過 ord() 還傳 'q' 的ASCII 的數值 讓 waitkey取的停止的參數
    if cv2.waitKey(10) == ord('q'):
        break
