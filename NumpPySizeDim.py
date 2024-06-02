#NumPy arrays have a fixed type. For example,
#assign x1[0] = 3.14159 will cause trucation

#x1[:3] # elements after index 3 including index 3

# middle elementes x1[1:4], not including index 4
# total number of elements 4 - 1 = 3


import numpy as np
rng = np.random.default_rng(seed=1701)

x1 = rng.integers(10, size =6)
x2 = rng.integers(10, size=(3,4))
x3 = rng.integers(10, size=(3,4,5))


print("x1\n", x1)
print("x2\n", x2)
print("x3\n", x3)

print("x3 ndim", x3.ndim) #dimension of x3 is x3, dimension of x2 is 2
print("x3 shape: ", x3.shape)
print("x3 size: ", x3.size)
print("x3 datatype: ", x3.dtype)
print()

print(x1)
print("x[i] example, x1[0]: ", x1[0])
print()

print(x2)
print("x[i,j] example, x2[2,0]", x2[2,3])
print()

print(x2)
print("x2[0,0]=12: ")
x2[0,0]=12
print(x2)

#NumPy arrays have a fixed type. For example,
#assign x1[0] = 3.14159 will cause trucation
print("x1: ", x1)
x1[0] = 3.14159
print(x1)
L=np.array([1,2,3,4])
L[1]=2.5
print(L[1])
print()
print()


#first three elements of x1
print(x1)
print("x1[:3]: ", x1[:3] )
print()

#elements after index 3
print(x1)
print("x1[3:]: ", x1[3:])
print()

# middle elementes x1[1:4], not including index 4
# total number of elements 4 - 1 = 3
print(x1)
print("x1[1:4]: ", x1[1:4])
print()

# Every second element
print(x1)
print("every second index of x1 starting from index 0, x1[::2]: ", x1[::2])
print()

# Every second element, starting at index1
print(x1)
print("every second index of x1 starting from index 1, x1[1::2]: ", x1[1::2])
print()

# all elements, reversed
print(x1)
print("all elements reversed", x1[::-1])
print()

# every second element from index 4, reversed
print(x1)
print("every second element from index 4, reversed, x1[4::-2]: ", x1[4::-2])


