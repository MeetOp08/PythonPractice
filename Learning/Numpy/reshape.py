import numpy as np

#Array Reshaping and Manipulation.

# reshape() – change the shape of an array.
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
print(data.shape)
reshape = data.reshape(4,3)
print(reshape)

#Reshape the array into 3 rows and 4 columns.
print(data.reshape(3,4))

# Reshape the array into 4 rows and 3 columns.
print(data.reshape(4,3))

# Reshape the array into 2 rows and 6 columns.
print(data.reshape(2,6))

# Try reshaping it into 5 rows and 2 columns. What happens, and why?
#print(data.reshape(5,2))#cannot reshape array of size 12 into shape (5,2)

# Reshape into 3 rows, letting NumPy calculate the columns.
print(data.reshape(3,-1))

# Reshape into 4 columns, letting NumPy calculate the rows.
print(data.reshape(-1,4))

# Reshape into a 3D array with 2 blocks, 2 rows, and automatically calculated columns.
print(data.reshape(2,2,-1))