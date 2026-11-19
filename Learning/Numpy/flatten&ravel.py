import numpy as np

# data = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])

# print(data.shape)

# result = data.flatten()
# print(result)
# result[0]=99
# print(result)#[[10 20 30]
#                 #[40 50 60]]
# print(data)#[10 20 30 40 50 60]
# #doesn't change the 0 index value in original array

# result1=data.ravel()
# print(result1)
# result1[0]=99
# print(result1)#[99 20 30 40 50 60]
# print(data)#[[99 20 30]
# #             [40 50 60]]
# #changes 0 index values in original array alse


numbers = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])




# Convert numbers into a 1D array using flatten().
print(numbers.flatten())

# Convert numbers into a 1D array using ravel().
print(numbers.ravel())

# Use flatten(), change the first element of the result to 999, and print both arrays. Does the original change?
result = numbers.flatten()
print(result)
result[0] = 999
print(result)
print(numbers)
#does not change original data

# Use ravel(), change the first element of the result to 999, and print both arrays. Does the original change?
result = numbers.ravel()
print(result)
result[0]=999
print(result)
print(numbers)
#changes original data