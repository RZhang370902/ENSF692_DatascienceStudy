import numpy as np
import pandas as pd

#use pandas to extract rainfall inches as a NumPy array
rainfall =  pd.read_csv('Seattle2014.csv')['PRCP'].values
inches = rainfall / 254.0 # 1/10mm -> inches
print(inches.shape)

#import matplotlib.pyplot as plt
#plt.hist(inches, 40)
#plt.show()
print()
x = np.array([1, 2, 3, 4, 5])
print(x)
print("x < 3", x < 3)
print(2 * x == x**2)
print()

rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))
print("x\n", x)
print("x < 6\n", x < 6)
print("np.count_nonzero(x<6)", np.count_nonzero(x<6))
print("np.sum(x<6)", np.sum(x<6))
print("np.sum(x<6, axis=1)", np.sum(x<6, axis=1))
print("np.all(x < 8, axis=1)", np.all(x < 8, axis=1))

#Boolean operators
print()
print("Boolean operators")
print(np.sum((inches > 0.5) & (inches < 1)))
print()
print("Number days without rain:        ", np.sum(inches == 0))
print("Number days with rain:           ", np.sum(inches !=0))
print("Days with more than 0.5 inches:  ", np.sum(inches > 0.5))
print("Rainy days with < 0.2 inches:    ", np.sum((inches > 0) & (inches < 0.2)))

print()
#Construct a mask of all rain days
rainy = (inches>0)

#Construct a mask of all summer days (June 21st is the 172nd day)
days = np.arange(365)
summer = (days > 172) & (days < 262)

print("Median precip on rainy days in 2014 (inches):        ",
      np.median(inches[rainy]))
print("Median precip on summer days in 2014 (inches):       ",
      np.median(inches[summer]))
print("Maximum precip on summer days in 2014 (inches:       )",
      np.max(inches[summer]))
print("Median precip on non-summer rainy days (inches):     ",
      np.median(inches[rainy & ~summer]))

