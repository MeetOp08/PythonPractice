import numpy as np

rainfall = np.array([120, 450, 800, 300, 950])

# What is the total rainfall?
print(np.sum(rainfall))

# What is the average rainfall?
print(np.mean(rainfall))

# What is the minimum rainfall?
print(np.min(rainfall))

# What is the maximum rainfall?
print(np.max(rainfall))

#Count the total number of rainfall measurements.
print(np.size(rainfall))

#Count how many rainfall values are greater than 500.
print(np.sum(rainfall>500))

#Find the total of rainfall values greater than 500.
print(np.sum(rainfall[rainfall>500]))

#Calculate the average of rainfall values below 500.
print(np.mean(rainfall[rainfall<500]))

