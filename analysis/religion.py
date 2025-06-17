import pandas as pd
import matplotlib.pyplot as plt

#Read the csv file
df = pd.read_csv('/Users/alexrosen/Laidlaw/data/prison_survey.csv')

'''
v2517: Rule Violations

Value Label
1 Yes
2 No
7 Don't know
8 Refused
9 (M) Blank
'''

'''
Original rule violation categories:
v2517
Yes           7217
No            7024
Blank          149
Refused         78
Don't know      31
Name: count, dtype: int64
'''
violation_categories = ['Yes', 'No', 'Blank', 'Refused', 'Don\'t know']
#create "dummy" variables -->  Ex:
#                               Yes:    F, F, F, F, T, F, F ;
#                               No :    T, T, T, T, F, F, F ;
#                               Blank,  F, F, F, F ,F, T, T ;
df_violation_dummies = pd.get_dummies(df['v2517'], prefix='violations')
print( df_violation_dummies)

#Adds violation dummies to df ( axis 1 means adds as new rows)
df = pd.concat([df, df_violation_dummies], axis=1)

### TODO Jan 12th 2025
'''
    Create a variable for "Yes" and "No" violations and then compare accross another factor: whether they are or are not part of a religious group


'''

#print(type(violation_dummies))
'''
for i in df_rule_violations:
    print(f'\n == \n')
    counter += i.value_counts()
    print(i.value_counts())
print(counter)
'''