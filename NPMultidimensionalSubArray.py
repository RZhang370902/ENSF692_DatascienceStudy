import numpy as np
rng = np.random.default_rng(seed=1701)

x2 = rng.integers(10, size =(3,4))
print(x2)
print()

# first two rows & three columns
print(x2)
print("first two rows & three columns, x2[:2,:3]: \n", x2[:2,:3])
print()

# three rows, every second column
print(x2)
print("first three rows, every second column, x2[:3, ::2]: \n",
      x2[:3,::2])
print()

# all rows & columns, reversed
print(x2)
print("all rows and columns, reversed, x2[::-1,::-1]: ")
print(x2[::-1,::-1])
print()

# first column of x2
print(x2)
print("first column of x2, x2[:,0]: ")
print(x2[:,0])
print()

# first row of x2
print(x2)
print("first row of x2, x2[0,:]: ")
print(x2[0,:])
print()

