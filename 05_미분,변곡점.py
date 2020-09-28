import numpy as np
import matplotlib.pyplot as plt
import cv2

def masks(vec):
    d = np.diff(vec)
    dd = np.diff(d)
    # mask = ((d[:-1] != 0) & (d[:-1] == -dd))
    mask = (d[:-1] == 0)
    # print(to_mask)
    return mask

Img = cv2.imread("GRAY.jpg")
dst = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
vec = np.average(dst,axis=0) # 세로축으로 합계

mask = masks(vec) # 마스크 생성
value = vec[1:-1][mask]
index = [i for i, value in enumerate(mask) if value == True]
print(index)

# point = apply_mask(to_mask,vec)
# print(point)
# print(apply_mask(to_mask,vec))

plt.figure(figsize=(12,6))
plt.plot(vec)
plt.plot(index,value)
plt.show()
print("완료")
