import numpy as np

# numpy can do full array calculation without for loop
print("np.arange(5):                    ", np.arange(5))
print("np.arange(1, 6):                 ", np.arange(1, 6))
print("np.arange(5)/np.arrange(1, 6)    ", np.arange(5)/np.arange(1, 6) )
print()

x = np.arange(9).reshape((3, 3))
print("x = np.arange(9).reshape((3,3 ))     ", x)
print("2 ** x                               ", 2 ** x)
print()

# Specifying Output
x= np.arange(5)
y = np.zeros(10)
np.power(2, x, out=y[::2])
print(y)
print()

#find sum of all elements in array
print("reduce")
x = np.arange(1, 6)
print(np.add.reduce(x))
print()
#find product of all elements in array
print(np.multiply.reduce(x))
print()

# accumulate output
print("accumulate")
print(np.add.accumulate(x))
print(np.multiply.accumulate(x))
print()

#outer
print("outer")
print(np.multiply.outer(x, x))
