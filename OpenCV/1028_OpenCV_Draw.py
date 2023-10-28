import cv2

# OpenCV 的顏色配置不是 RGB，是BGR
# 所以(255,0,0)不是紅色，是藍色
# 如果解析度 1024*768，那麼代表有786,432個點
# X做標示 0-1024，Y座標是 0~768
# X座標增加，則點會往右移動。Y座標增加，則點會往下面移動


img = cv2.imread("bg.jpg")

# 畫一條從(50,50)到(200,50)的直線，顏色是紅色(0,0,255)，寬度是3
cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 3)

# 畫矩形的時候，需要給予對角線的起點以及終點
# 換句話說，也就是矩形的左上與右下兩個點
cv2.line(img, (50, 75), (200, 100), (0, 0, 255), 3)
cv2.rectangle(img, (50, 75), (200, 100), (0, 0, 255), 3)

cv2.namedWindow("test")
cv2.imshow("test", img)
cv2.imwrite("today.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
