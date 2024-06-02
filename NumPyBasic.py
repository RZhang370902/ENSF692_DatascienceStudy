import numpy as np

new_matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(new_matrix)
print(np.__version__)

#basic NumPy array
L = np.array([1, 4, 2, 5, 3])
print("\n")
print(L)

#NumPy will upcast if possible
L = np.array([3.14, 4, 2, 5, 3])
print("\n")
print(L)

#NumPy explicitly set the data type of the resulting array
L = np.array([1, 4, 2, 5, 3], dtype='float32')
print("\n")
print(L)

# nested lists result in multi-dimensional arrays
L = np.array([range(i, i + 3) for i in [2, 4, 6]])
print("\n")
print(L)

# Create a length-10 integer array filled with zeros
L=np.zeros(10,dtype=int)
print("\n")
print(L)

# Create a 3x5 floating-point array filled with ones
L=np.ones((3,5),dtype=float)
print("\n")
print(L)

# Create a 3x5 array filled with 3.14
L=np.full((3, 5), 3.14)
print("\n")
print(L)

# Create an array filled with a linear sequence
# Starting at 0, ending at 20, steping by 2
# (this is similar to the build-in-range() function)
L=np.arange(0, 20, 2)
print("\n")
print(L)

# Create an array of five values evenly spaced between 0 and 1
L=np.linspace(0,1,5)
print("\n")
print(L)

# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
L=np.random.random((3,3))
print("\n")
print(L)

# Create a 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
L=np.random.normal(0,1,(3,3 ))
print("\n")
print(L)

# Create a 3x3 array of random integers in the interval [0,10]
L=np.random.randint(0,10,(3,3,3))
print("\n")
print(L)

# Create a 3x3 identity matrix
L=np.eye(3)
print("\n")
print(L)

# Create an uninitialized array of three integers
# The values will be whatever happens to already exist at that memory location
L=np.empty(3)
print("\n")
print(L)

# NumPy datatype
L=np.zeros(10, dtype=np.bool_)
print("\n")
print(L)

L = [1, 2, 3]
B = L
B += B
print(L)

#20.0 is not integer, 20 is
L = [n//2 for n in range(0,100,10)]
print(L)