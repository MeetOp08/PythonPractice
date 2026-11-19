import numpy as np

# np.vstack() and np.hstack()
# Before learning these functions, remember:
# - vstack = Vertical Stack (one array above another).
# - hstack = Horizontal Stack (one array beside another).
# Both functions are used to combine arrays.


# a = np.array([10, 20, 30])
# b = np.array([40, 50, 60])

# result = np.vstack((a, b))
# result1 = np.concatenate((a,b))
# print(result)
# print(result.shape)

# print(result1)
# print(result1.shpae)

# a = np.array([10, 20, 30])
# b = np.array([40, 50, 60])

# result = np.hstack((a, b))

# print(result)
# print(result.shape)

# a = np.array([
#     [10, 20],
#     [30, 40]
# ])

# b = np.array([
#     [50, 60],
#     [70, 80]
# ])

# result = np.vstack((a, b))
# print(result)

# a = np.array([
#     [10, 20],
#     [30, 40]
# ])

# b = np.array([
#     [50, 60],
#     [70, 80]
# ])

# result = np.hstack((a, b))
# print(result)
# print(result.shape)


a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

# Exercise 1: Use np.vstack() to combine both arrays. What is the output shape?
result = np.vstack((a,b))
print(result)
print(result.shape)

# Exercise 2: Use np.hstack() to combine both arrays. What is the output shape?
result = np.hstack((a,b))
print(result)
print(result.shape)


x = np.array([
    [1, 2],
    [3, 4]
])

y = np.array([
    [5, 6],
    [7, 8]
])


# # Exercise 3: Use np.vstack() and print the result.
# print(np.vstack((x,y)))

# # Exercise 4: Use np.hstack() and print the result.
# print(np.hstack((x,y)))

# # Exercise 5: Explain the difference between vstack() and hstack() in your own words.
# vstack --> vertically combine array
# hstack --> horizontally combine array