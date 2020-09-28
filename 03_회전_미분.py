import numpy as np
import matplotlib.pyplot as plt
import cv2

# Img = cv2.imread("TEST_IMG.jpg")
Img = cv2.imread("apple.jpg")
print(Img)
height, width, channel = Img.shape
print(Img.shape)
matrix = cv2.getRotationMatrix2D((width/2, height/2), 40, 1)
dst = cv2.warpAffine(Img, matrix, (width, height))

# cv2.imshow("src",Img)
# cv2.imshow("dst",dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


dst = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
dst_1D = np.average(dst,axis=0)
# np.aver
print(dst_1D)

dst_1D_GR = np.gradient(dst_1D,0.1)
dst_1D_GR_ABS = np.abs(dst_1D_GR)

plt.figure(figsize=(12,6))
plt.plot(dst_1D_GR_ABS)
plt.plot(dst_1D_GR)
plt.plot(dst_1D)
plt.show()
print("완료")
print(np.max(dst_1D_GR), np.argmax(dst_1D_GR))

np.argpartition(dst_1D_GR,2)