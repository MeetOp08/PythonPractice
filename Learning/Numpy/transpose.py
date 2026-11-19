import numpy as np

# 1. What is transpose?
# Transpose means converting rows into columns and columns into rows.

# data = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])

# print(data)
# print(data.shape)

# result = np.transpose(data)
# print(result)
# print(result.shape)

# print(data.T)
# print(data.T.shape)
# print(data)

numbers = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
])

# # Print the original shape of numbers.
# print(numbers.shape)

# # Transpose the array using np.transpose().
# print(np.transpose(numbers))

# # Transpose the array using .T.
# print(numbers.T)

# # Print the shape after transpose.
# print(numbers.T.shape)
# print(np.transpose(numbers).shape)

# # Explain in your own words what happened to the rows and columns.
# # row changes to column
# # columns changes to row

result = numbers.T
result[0,0] = 99
print(result)
print(numbers)

result = np.transpose(numbers)
result[0,0] = 999
print(result)
print(numbers)

#changes happen in original array