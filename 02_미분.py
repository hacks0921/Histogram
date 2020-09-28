import numpy as np
import matplotlib.pyplot as plt
import cv2

Img = cv2.imread("GRAY.jpg")
dst = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
dst_1D = np.average(dst,axis=0)
# np.aver
# print(dst_1D)

dst_1D_GR = np.gradient(dst_1D,0.1)
# dst_1D_GR  = np.diff(dst_1D_GR)
# mask = ((d[:-1] != 0) & (d[:-1] == -dd))

mask = dst_1D_GR[:] == 0
value = dst_1D[:][mask]
index = [i for i, value in enumerate(mask) if value == True]
print(value)
print(index)

plt.figure(figsize=(12,6))
# plt.plot(dst_1D_GR_ABS)
plt.plot(dst_1D_GR)
plt.plot(dst_1D)
plt.scatter(index, value)
plt.show()
print("완료")

