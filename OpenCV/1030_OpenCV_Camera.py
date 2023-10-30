import time

import cv2

path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
print(path)

# 宣告 OpenCV 的分類器
faceCascade = cv2.CascadeClassifier(path)

camera = cv2.VideoCapture(0)
cv2.namedWindow("Video")
# 如果攝影機本身是可以抓到的，那麼才要執行下列動作
while camera.isOpened():
    # 驗證攝影機本身是否可以提供畫面
    # 如果可以，hassignal 就會回傳 True，img才會有畫面
    # 相反，hassignal 就會回傳 False，img 會是 Null
    hassignal, img = camera.read()
    if hassignal:
        faces = faceCascade.detectMultiScale(img, scaleFactor=1.1,
                                             minNeighbors=5, minSize=(30, 30),
                                             flags=cv2.CASCADE_SCALE_IMAGE)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Video", img)
        # 不一定每一台電腦都要用sleep，即時刷新的要看電腦的執行速度
        # 如果執行速度比較不夠力，那麼就可以搭配這個函數降低採樣率
        # time.sleep(0.1)
        # 通常1秒攝影機會回傳 60 個 frame
        # waitKey(3) 的意思是每隔 3 個 frame 採樣一次
        # 差不多 1/20 秒
        input_key = cv2.waitKey(3)  # 取樣鍵盤按了什麼東西
        # 設計一個機制，跳出上方的 while 迴圈，不然畫面會持續刷新，
        if input_key == ord('x') or input_key == ord('X'):
            break
        if input_key == ord('c') or input_key == ord('C'):
            if hassignal:
                faces = faceCascade.detectMultiScale(img, scaleFactor=1.1,
                                                     minNeighbors=5, minSize=(30, 30),
                                                     flags=cv2.CASCADE_SCALE_IMAGE)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.imwrite("photo.jpg", img)

camera.release()
cv2.destroyAllWindows()
