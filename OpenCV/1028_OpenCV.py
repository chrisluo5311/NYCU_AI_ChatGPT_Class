import cv2

# 彩色組: 預設使用 cv2.IMREAD_COLOR
cv2.namedWindow("testImage")
img = cv2.imread("MJ.png", cv2.IMREAD_COLOR)
cv2.imshow("testImage", img)

# 彩色圖片可以變灰階，但灰階圖片無法變回彩色
# 灰階組: cv2.IMREAD_GRAYSCALE-灰階
cv2.namedWindow("testImage_G")
img_G = cv2.imread("MJ.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("testImage_G", img_G)
# cv2.imwrite("./MJ_G.png", img_G)
# cv2.imwrite("./MJ_G.jpg", img_G)
# cv2.imwrite("./MJ_G_Low.jpg", img_G,
#             [int(cv2.IMWRITE_JPEG_QUALITY), 50])  # jpg格式特色: 可以壓縮圖片，但畫質差一點

cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
