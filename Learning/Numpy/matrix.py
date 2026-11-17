import numpy as np

# oneDarray=np.array([20,39,74,21,53])
# print("1 Dimentional:",oneDarray.ndim)
# print(oneDarray.shape)
# print(oneDarray.size)

# twoDarray = np.array([
#     [10,20,30,40,50],
#     [60,70,80,90,100]
# ])
# print("2 Dimentinal:",twoDarray.ndim)
# print(twoDarray.shape)
# print(twoDarray.size)

# threeDarray = np.array([
#     [
#         [10,20,30,40,50],
#         [60,70,80,90,100]
#     ],
#     [
#         [100,90,80,70,60],
#         [50,40,30,20,10]
#     ]
# ])

# print("33 Dimentinal:",threeDarray.ndim)
# print(threeDarray.shape)
# print(threeDarray.size)

# print(oneDarray[1])

# data = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# # Exercise A — Basic indexing
# # 1. Print 10.
# # 2. Print 50.
# # 3. Print 90.
# # 4. Print 60.
# print(data[0,0])
# print(data[1,1])
# print(data[2,2])
# print(data[1,2])

# # Exercise B — Negative indexing
# # 5. Print the last element of the array.
# # 6. Print the last element of the second row.
# print(data[-1,-1])
# print(data[1,-1])

# # Exercise C — Understanding
# # 7. What does data[0, 2] return?-->30
# # 8. What does data[2, 0] return?-->70
# # 9. What happens if you write data[3, 0]? Explain why.-->index 3 is out of bounds for axis 0 with size 3





# data = np.array([10, 20, 30, 40, 50, 60, 70, 80])
# # Exercise A — 1D slicing
# # 1. Extract [20, 30, 40].
# # 2. Extract [50, 60, 70, 80].
# # 3. Extract [10, 30, 50, 70].
# # 4. Reverse the entire array.

# print(data[1:4])
# print(data[4:])
# print(data[::2])

# data2 = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120]
# ])

# # Exercise B — 2D slicing
# # Extract the first two rows.
# print(data2[0:2])
# print(data2[:-1,])

# # Extract the last two columns.
# print(data2[:,-2:])

# # Extract:[[20, 30],
# #  [60, 70]]
# print(data2[0:2,1:3])

# # Extract the complete second row.
# print(data2[1,:])



# rainfall = np.array([120, 450, 800, 300, 950, 600, 150, 720, 1000, 400])

# #Extract rainfall values greater than 500.
# print(rainfall[rainfall>500])

# #Extract rainfall values less than 400.
# print(rainfall[rainfall<400])

# #Extract rainfall values equal to 600.
# print(rainfall[rainfall==600])

# #Extract rainfall values not equal to 300.
# print(rainfall[rainfall!=300])

# #Extract values greater than or equal to 600.
# print(rainfall[rainfall>=600])

# #Extract values between 300 and 800, including both boundaries.
# print(rainfall[(rainfall>=300) & (rainfall<=800)])

# #Extract values below 200 OR above 900.
# print(rainfall[(rainfall<200) | (rainfall>900)])

# #Find the index positions of values greater than 700.
# print(np.where(rainfall>700))

# #Replace values below 400 with zero, keeping other values unchanged.
# print(np.where(rainfall<400,0,rainfall))

# #Count how many rainfall measurements are greater than 500.
# print(np.sum(rainfall>500))

# #Count how many rainfall values are less than 400.
# print(np.sum(rainfall<400))

# #Replace all values greater than 800 with 800, keeping the remaining values unchanged.
# print(np.where(rainfall>800,800,rainfall))

# #Extract values that are either greater than 500 AND less than 900.
# print(rainfall[(rainfall>500)&(rainfall<900)])

rainfall = np.array([120, 450, 800, 300, 950])

vadodara = np.array([120, 450, 800, 300, 950])

ahmedabad = np.array([100, 400, 700, 350, 900])

#Add 50 to every rainfall value.
print(rainfall+50)

#Subtract 100 from every rainfall value.
print(rainfall-100)

#Multiply every rainfall value by 2.
print(rainfall*2)

#Divide every rainfall value by 5.
print(rainfall/5)

#Add Vadodara and Ahmedabad rainfall arrays element by element.
print(vadodara+ahmedabad)

#Find the difference between Vadodara and Ahmedabad rainfall at each matching position.
print(vadodara-ahmedabad)

#Multiply the two city arrays element by element.
print(vadodara*ahmedabad)

#Check whether the original rainfall array changes when you execute result = rainfall + 100. Print both arrays.
result = rainfall + 100
print(result)
print(rainfall)