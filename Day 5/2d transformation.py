import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("Goose.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#2D TRANSFORMATION
M = np.float32([[1,0,50],[0,1,50]])
translated = cv2.warpAffine(img,M,(img.shape[1], img.shape[0]))
#2D ROTATION
M = cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2),45,1)
rotated = cv2.warpAffine(img,M, (img.shape[1],img.shape[0]))
# show results
titles = ["Original","Translated","Rotated"]
images = [img, translated, rotated]
for i in range(3):
    plt.subplot(2,2,i+1),plt.imshow(images[i]), plt.title(titles[i])
    plt.axis("off")
plt.show()