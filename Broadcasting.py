# add multidimensional arrays that match in one dimension
import numpy as np
a = np.array([0 ,1 ,2])
b = np.array([5, 5, 5])
M = np.ones((3, 3))
print("np.ones((3, 3)): \n", M)
print()
print("M + a: \n", M + a)
print()

a = np.arange(3)
b = np.arange(3)[:, np.newaxis]
print(a)
print(b)
print(a + b)

#Rules of Broadcasting

#Broadcasting in NumPy follows a strict set of rules to determine the interaction between the two arrays:

#Rule 1: If the two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is padded with ones on its leading (left) side.
#Rule 2: If the shape of the two arrays does not match in any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape.
#Rule 3: If in any dimension the sizes disagree and neither is equal to 1, an error is raised.

b = np.arange(3)
print(b)
print(b.shape)
print()

M = np.ones((1, 2, 3))
print(M)
print()

a = np.arange(3).reshape((3, 1))
b = np.arange(3)
print(a)
print()
print(b)
print()

M = np.ones((3, 2))
a = np.arange(3)
print(M + a[:, np.newaxis])
print()

rng = np.random.default_rng(seed=1701)
x = rng.random((10, 3))
print(x)

Xmean = x.mean(0)
print(Xmean)
print(x - Xmean)


print()
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]
print(x)
print(y)

z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

import matplotlib.pyplot as plt

plt.imshow(z, origin='lower', extent=[0, 5, 0, 5])
plt.colorbar()
plt.show()


