import numpy as np

grid = np.arange(1,10)
print("grid: ", grid)
grid = grid.reshape(3,3)
print("grid.reshape(3,3)\n", grid)


#np.newaxis
x = np.array([1, 2, 3])
print(x[np.newaxis, :])
print(x[:, np.newaxis])

# Concatenation of Arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(np.concatenate([x, y]))

# Concatenate through axis
print()
print("Concatenate through axis")
grid = np.array([[1, 2, 3],
                 [4, 5 ,6]])
print(np.concatenate([grid, grid], axis=1))

# stack the arrays, size matters
print()
print("vertically stack the arrays")
print("x: ", x)
print("grid: ", grid)
print(np.vstack([x, grid]))
print()
print("horizontally stack the arrays")
y = np.array([[99],
              [99]])
print(np.hstack([grid, y]))

# splitting of array
print()
print("normal split")
x = [1, 2 ,3, 99, 99, 3, 2, 1]
#first 3, first 5, and the rest
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2 , x3)

print()
print("grid")
grid = np.arange(16).reshape((4,4))
print(grid)
print()
print("multidimensional split")
upper, lower = np.vsplit(grid, [2])
left, right = np.hsplit(grid, [2])
print()
print("left, right")
print(left, "\n", right)
print()
print("upper, lower")
print(upper, "\n", lower)






