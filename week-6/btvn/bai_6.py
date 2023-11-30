import numpy as np
import matplotlib.pyplot as plt

width = np.array([[50,75,80,60,70,100,65,85]]).T  # traindata
prices = np.array([[600,860,930,700,800,1150,750,970]]).T

plt.plot(width,prices , 'ro')
plt.xlabel('width(m2)')
plt.ylabel('prices(triệu đô)')
# plt.show()

# => đồ thị là đường thẳng nên prices = w_1 * width + w_0
one = np.ones((width.shape[0], 1))
print(one)
widthbar = np.concatenate((one,width) , axis= 1)
# print(pricesbar)
A = np.dot(widthbar.T, widthbar)
# print(A)
b = np.dot(widthbar.T, prices)
w = np.dot(np.linalg.pinv(A), b)
# print("w: ",w)

w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(45,105,2)
y0 = w_0 + w_1*x0

plt.plot(width.T, prices.T , 'ro')
plt.plot(x0,y0)
plt.show()
print(w_1*105 + w_0)