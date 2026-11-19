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

data = np.array([
    [10, 20],
    [30, 40]
])

print(np.append(data,[20,50]))#default axis = None so it will return flatten array(1D array)

new_data = np.array([
    [30,20]
])

print(np.append(data,new_data,axis=0))
