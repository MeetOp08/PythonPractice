import numpy as np


# rainfall = np.array([120, 150, 180, 200,220, 250, 280, 300,320, 350, 380, 400])

# print(rainfall)
# print(np.split(rainfall,3))

# # What happened?
# # - Original array contains 12 elements.
# # - We divided it into 3 equal parts.
# # - Each part contains 4 elements.

# # Splitting using positions
# # What if you don't want equal groups?
# data = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# result = np.split(data,[2,5])
# print(result)

# # Let's understand the positions:
# # - First split at index 2.
# # - Second split at index 5.
# # - The remaining elements form the final array.

# data = np.array([
#     [10, 20],
#     [30, 40],
#     [50, 60],
#     [70, 80]
# ])

# result = np.split(data,2,axis=0)
# print(result)


# result1 = np.split(data,2,axis=1)
# print(result1)


data = np.array([10, 20, 30, 40, 50, 60, 70, 80])
# Exercise 1 — Equal splitting
# Split this array into 4 equal parts using np.split().
print(np.split(data,4))

# Exercise 2 — Unequal splitting
# Using the same array, split it at positions 2 and 5.
print(np.split(data,[2,5]))

# Exercise 3 — 2D row splitting
numbers = np.array([
    [10, 20],
    [30, 40],
    [50, 60],
    [70, 80]
])

# Split this array into 2 equal parts along axis=0.
print(np.split(numbers,2,axis=0))

# Exercise 4 — 2D column splitting
# Using the same numbers array, split it into 2 equal parts along axis=1.
print(np.split(numbers,2,axis=1))

# Exercise 5 — Understanding
# If an array has 15 elements, can you split it into 4 equal parts using np.split()? Explain why.
# i think no cus qe can not devide 15 is odd so it can not devide into 4 equal part

