import numpy as np

# 1. Create an array containing 10, 20, 30, 40, 50

data = np.array([10,20,30,40,50])
print(data)

# 2. Create an array containing five zeros
data_zeros=np.zeros(5)
print(data_zeros)

# 3. Create an array containing six ones
data_ones = np.ones(6)
print(data_ones)

# 4. Create an array containing five values of 100
fivedata = np.full(5,100)
print(fivedata)

# 5. Create an array containing numbers from 1 to 20
print(np.arange(1,21,5))

# 6. Create an array containing 10 equally spaced values
#    between 0 and 100
print(np.linspace(0,100,10))