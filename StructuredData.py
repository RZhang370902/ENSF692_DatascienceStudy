import numpy as np

name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

x = np.zeros(4, dtype=int)

# Use a compound data type for structured arrays

data = np.zeros(4, dtype={'names':('name', 'age', 'weight'), 'formats':('U10', 'i4', 'f8') })
print(data.dtype)
data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)
print(data['name'])
print(data['name'][-1])
print(data[data['age'] < 30]['name'])

print()
print("2")
data = np.zeros(4, dtype=[('name', 'U10'),('age', 'i4'),('weight', 'f8')])
print(data.dtype)
data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)
print(data['name'])
print(data['name'][-1])
print(data[data['age'] < 30]['name'])
print("2")