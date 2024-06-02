import numpy as np

mean = [0, 0]
cov = [[1, 2],
       [2, 5]]
X = np.random.multivariate_normal(mean, cov, 100)
print(X.shape)

import matplotlib.pyplot as plt
#plt.scatter(X[:, 0], X[:, 1])
#plt.show()

indices = np.random.choice(X.shape[0], 20, replace=False)
print(indices)
selection = X[indices] # fancy indexing here
plt.scatter(X[:, 0], X[:, 1], alpha=0.1)
plt.scatter(selection[:, 0], selection[:, 1], facecolor='black', s=200)
plt.show()