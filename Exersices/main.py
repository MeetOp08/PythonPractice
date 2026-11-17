import pandas as pd

tips = pd.read_csv('tips.csv')

#print(tips.query('total_bill > 40'))

#print(tips.query("sex == 'Female' and smoker == 'Yes' and day == 'Sun'"))



print(tips.query("day == 'Sun' or day =='Sat' "))
print(tips.query ("day in ['Sun', 'Sat']"))


print(tips[(tips['size'] >= 5) & (tips['time'] == 'Dinner')])
print(tips.query("size >= 5 and time == 'Dinner'"))

print(tips.nlargest(5,'tip'))
print(tips.nsmallest(5,'tip'))

print(tips.sort_values('tip',ascending = False).head(5))

print(tips.sort_values(['tip','size'],ascending = [True,False]).loc[:, ['tip','size']])