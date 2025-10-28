import pandas as pd
import matplotlib.pyplot as plt

#Read the csv file
df = pd.read_csv('/Users/alexrosen/Laidlaw/data/prison_survey.csv')

'''
v2509 -> S10Q12A_1: Since your admission to prison on [MOST RECENT ADMISSION DATE], have you
joined or participated in - A Bible club or other religious study group (including Muslims)?

V2517 --> S10Q13A: Since your admission [MOST RECENT ADMISSION DATE], have you been written up
or found guilty of breaking any of the prison rules?
'''

''' 
Changes to Template
v2509 --> question used
plt.title
plt.title (again)
'''

survey_responses = ['Yes', 'No', 'Don\'t know','Refused', 'Blank']

# Creates data frame for "YES category"
yescategory = df[df['v2509'] == 'Yes']

# Gets the counts by each of the violation answer categories
yc_yv = yescategory['v2517'].value_counts().get('Yes', 0)
yc_nv = yescategory['v2517'].value_counts().get('No', 0)
yc_dkv = yescategory['v2517'].value_counts().get('Don\'t know', 0)
yc_rv = yescategory['v2517'].value_counts().get('Refused', 0)
yc_bv = yescategory['v2517'].value_counts().get('Blank', 0)

# Calculates Percentages
yescategory_count = yc_yv + yc_nv + yc_dkv + yc_rv + yc_bv

yc_percentages = [
    yc_yv / yescategory_count, 
    yc_nv / yescategory_count, 
    yc_dkv / yescategory_count, 
    yc_rv / yescategory_count,
    yc_bv / yescategory_count]


# Plotting Category
plt.subplot(1,2,1)
bars1 = plt.bar(survey_responses, yc_percentages)
plt.ylabel("% of Total")
plt.title("Rule Violations By Category Group Members")
plt.bar_label(
    bars1,
    labels=[f"{x:.1%}" for x in yc_percentages],  
    padding=3, 
    fontsize=9 
)


# Creates data frame for "NO category"
nocategory = df[df['v2509'] == 'No']

# Gets the counts by each of the violation answer categories
nc_yv = nocategory['v2517'].value_counts().get('Yes', 0)
nc_nv = nocategory['v2517'].value_counts().get('No', 0)
nc_dkv = nocategory['v2517'].value_counts().get('Don\'t know', 0)
nc_rv = nocategory['v2517'].value_counts().get('Refused', 0)
nc_bv = nocategory['v2517'].value_counts().get('Blank', 0)

# Calculates Percentages
nocategory_count = nc_yv + nc_nv + nc_dkv + nc_rv + nc_bv

nc_percentages = [
    nc_yv / nocategory_count, 
    nc_nv / nocategory_count, 
    nc_dkv / nocategory_count, 
    nc_rv / nocategory_count,
    nc_bv / nocategory_count]

# Plotting Category
plt.subplot(1,2,2)
bars2 = plt.bar(survey_responses, nc_percentages)
plt.ylabel("% of Total")
plt.title("Rule Violations By NON-Category Group Members")
plt.bar_label(
    bars2,
    labels=[f"{x:.1%}" for x in nc_percentages],  
    padding=3, 
    fontsize=9 
)

plt.show()