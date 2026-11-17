#filtering rows using conditions.

import pandas as pd

data = {

        "Name":["Meet","Raj","Krishna","Jainil","Eman","Jay"],
        "Age":[21,21,22,24,21,20],
        "City":["Vadodara","Navssari","Gandhinagar","Ahmedabad","Mahesana","Surat"],
        "Percenatge":[79.7,80.0,76.3,90.7,69.0,88.8]
       }

df = pd.DataFrame(data)

#print(df[df['Percenatge']>85]) 
#print(df['City'] == 'Surat')#This produces True or False for each row.

# print(df[df['Age'] == 21])
# print(df[df['City'] == 'Vadodara'])
# print(df[df['Percenatge'] >= 85 ])

#Combining conditions with & and |
print(df[df['City'] == 'Surat' | df['Percenatge']>80])


