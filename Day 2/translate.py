import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread("tree and moon.jpg")
rows,cols=img.shape[:2]

circle = cv2.circle(img,(100,100),50,(0,0,255),3)


M = np.float32([[1,0,-10],[0,1,0]])
translate = cv2.warpAffine(img,M,(cols,rows))
plt.imshow(cv2.cvtColor(translate,cv2.COLOR_BGR2RGB))
plt.show()