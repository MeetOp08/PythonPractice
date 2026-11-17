import pandas as pd

data = {

        "Name":["Meet","Raj","Krishna","Jainil","Eman","Jay"],
        "Age":[21,21,22,24,21,20],
        "City":["Vadodara","Navssari","Gandhinagar","Ahmedabad","Mahesana","Surat"],
        "Percenatge":[79.7,80.0,76.3,90.7,69.0,88.8]
       }

df = pd.DataFrame(data)

# print(df)


#shape
#print("Shape:",df.shape)

#head
# print("First 3 rows:")
# print(df.head(3))

#tail
# print("Last 3 rows:")
# print(df.tail(3))

#info
# print("Dataset information:")
# print(df.info)

#describe
# print("Statistical summary:")
# print(df.describe)

# #Columns
# print("Column names:")
# print(df.columns)

# #dtype
# print("Data types:")
# print(df.dtypes)

# print(df['City'])#returns a series
# print(df[['City']])#returns a dataframe
#print(df[["Name","City"]])#Returns multiple columns as a DataFrame