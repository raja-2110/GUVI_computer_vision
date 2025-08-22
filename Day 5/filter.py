import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("goose.jpg")

blur = cv2 .blur(img, (10,9))
gaussian = cv2.GaussianBlur(img, (15,5),0)
median = cv2.medianBlur(img, 7)

title = ["Original", "Blur", "Gaussian","Median"]
images= [img,blur,gaussian,median]
for i in range(4):
    plt.subplot(2,2,i+1), plt.imshow(images[i]),plt.title(title[i])
    plt.axis("off")
plt.show()