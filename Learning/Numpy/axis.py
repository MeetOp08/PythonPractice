import numpy as np

# rainfall = np.array([
#     [120, 150, 200, 180],
#     [100, 130, 170, 160],
#     [140, 160, 220, 190]
# ])

# # Total rainfall for each city.
# print(np.sum(rainfall,axis=1))

# # Average rainfall for each city.
# print(np.mean(rainfall,axis=1))

# # Total rainfall for each month across all cities.
# print(np.sum(rainfall,axis=0))

# # Average rainfall for each month across all cities.
# print(np.mean(rainfall,axis=0))

sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400],
    [250, 350, 450]
])

# Calculate total sales for each salesperson.
print(np.sum(sales,axis=1))

# Calculate average sales for each salesperson.
print(np.mean(sales,axis=1))

# Calculate total sales for each month.
print(np.sum(sales,axis=0))

# Calculate average sales for each month.
print(np.mean(sales,axis=0))

# Find the highest sales value in each salesperson's row.
print(np.max(sales,axis=0))

# Find the lowest sales value in each month.
print(np.min(sales,axis=1))