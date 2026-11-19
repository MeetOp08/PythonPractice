import numpy as np


# 1. What is concatenate?
# concatenate() means joining two or more arrays together.

# Imagine you have two datasets:
# - Dataset A contains January sales.
# - Dataset B contains February sales.
# You want to combine them into one array. NumPy provides np.concatenate() for this.

# a = np.array([10, 20, 30])
# b = np.array([40, 50, 60])

# result = np.concatenate((a, b))

# print(result)


# a = np.array([
#     [10, 20],
#     [30, 40]
# ])

# b = np.array([
#     [50, 60],
#     [70, 80]
# ])

# result = np.concatenate((a,b),axis = 0)
# print(result)
# print(result.shape)

# result = np.concatenate((a,b),axis = 1)
# print(result)
# print(result.shape)

x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

y = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

# What will be the output of np.concatenate((x, y), axis=0)?
# [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [10, 11, 12]]
# What will be the shape of the output?
#(4,3)

# Will np.concatenate((x, y), axis=1) work? Explain why.
# [1, 2, 3,7, 8, 9],
# [4, 5, 6,10, 11, 12]