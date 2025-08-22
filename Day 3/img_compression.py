import cv2

img= cv2.imread("image 2.jpeg")

cv2.imwrite("compresed_image_30.jpeg",img,[int(cv2.IMWRITE_JPEG_QUALITY),30])
cv2.imwrite("compresed_image_90.jpeg",img,[int(cv2.IMWRITE_JPEG_QUALITY),90])
