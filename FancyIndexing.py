import numpy as np
rand = np.random.RandomState(42)

x = rand.randint(100, size=10)
print(x)
ind = [3, 7 ,4]
print(x[3], x[7], x[4])
print(x[ind])
print(x[[3, 7 ,4]])
ind = [[3, 7],
       [4, 5]]
#index can be used to reshape array
print(x[ind])
print()

X = np.arange(12).reshape((3, 4))
print(X)
row = np.array([0 ,1 ,2])
col = np.array([2 ,1 ,3])
print(X[row, col])

#Combined Indexing
print(X)
print(X[2, [2, 0, 1]])
print(X[1:,[2, 0 ,1]])
mask = np.array([1, 0, 1, 0], dtype=bool)
print(X[row[:, np.newaxis], mask])