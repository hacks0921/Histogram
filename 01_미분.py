import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

t = np.arange(0, 2*np.pi, 0.1)
y1 = np.sin(t)

plt.figure(figsize=(12,6))
plt.plot(t, y1)
plt.show()

def derivative(f, a, h=0.01):
    return (f(a + h) - f(a))/h

dy1dx = derivative(np.sin, t)

plt.figure(figsize=(12,5))
plt.plot(t, dy1dx, 'r.', label='Calculated Difference')
plt.plot(t, np.cos(t), 'b', label='True Value')
plt.plot(t, y1, 'k', label='Original Value')
plt.legend(loc='best')
plt.show()

print("완료")