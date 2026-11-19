import numpy as np

# 1. What is np.append()?
# np.append() is used to add new elements to an existing NumPy array.

import numpy as np

# rainfall = np.array([120, 150, 180])
# result = np.append(rainfall,200)
# result1 = np.append(rainfall,[200,300,400])
# print(result)
# print(result1)
# print(rainfall)

# data = np.array([
#     [10, 20],
#     [30, 40]
# ])

# #print(np.append(data,[20,50]))#default axis = None so it will return flatten array(1D array)

# new_data = np.array([
#     [30,20],[10,40]
# ])

# print(np.append(data,new_data,axis=0))

# print(np.append(data,new_data,axis=1))  


# #Exercise 1 — Add one element
# rainfall = np.array([100, 200, 300, 400])
# #Add 500 using np.append().
# print(np.append(rainfall,500))

# # Exercise 2 — Add multiple elements
# # Using the same rainfall array, add 500, 600, and 700 together.
# print(np.append(rainfall,[500,600,700]))

# numbers = np.array([10, 20, 30])
# # Append 40 into a variable named result.
# # Print both numbers and result. Explain why their outputs are different.

# result = np.append(numbers,40)
# print(result)
# print(numbers)

# #original array does not change

# # Exercise 4 — Add a row

# data = np.array([
#     [10, 20],
#     [30, 40]
# ])

# print(np.append(data,[[50,60]],axis=0))
# #Exercise 5 — Add a column
# #Using the same data, add a new column containing:
# print(np.append(data,[[50],[60]],axis=1)) 