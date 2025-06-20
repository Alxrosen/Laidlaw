import pandas as pd
import matplotlib.pyplot as plt

#Read the csv file
df = pd.read_csv('/Users/alexrosen/Laidlaw/data/prison_survey.csv')

'''
2509 -> religious group
2517 --> rule violations
'''
survey_responses = ['Yes', 'No', 'Don\'t know','Refused', 'Blank']

# Creates data frame for "YES religion"
yesreligion = df[df['v2509'] == 'Yes']

# Gets the counts by each of the violation answer categories
yr_yv = yesreligion['v2517'].value_counts().get('Yes', 0)
yr_nv = yesreligion['v2517'].value_counts().get('No', 0)
yr_dkv = yesreligion['v2517'].value_counts().get('Don\'t know', 0)
yr_rv = yesreligion['v2517'].value_counts().get('Refused', 0)
yr_bv = yesreligion['v2509'].value_counts().get('Blank', 0)

# Calculates Percentages
yesreligion_count = yr_yv + yr_nv + yr_dkv + yr_rv + yr_bv

yr_percentages = [
    yr_yv / yesreligion_count, 
    yr_nv / yesreligion_count, 
    yr_dkv / yesreligion_count, 
    yr_rv / yesreligion_count,
    yr_bv / yesreligion_count]


# Plotting Religious
plt.subplot(1,2,1)
bars1 = plt.bar(survey_responses, yr_percentages)
plt.ylabel("% of Total")
plt.title("Rule Violations By Religious Group Members")
plt.bar_label(
    bars1,
    labels=[f"{x:.1%}" for x in yr_percentages],  
    padding=3, 
    fontsize=9 
)


# Creates data frame for "NO religion"
noreligion = df[df['v2509'] == 'No']

# Gets the counts by each of the violation answer categories
nr_yv = noreligion['v2517'].value_counts().get('Yes', 0)
nr_nv = noreligion['v2517'].value_counts().get('No', 0)
nr_dkv = noreligion['v2517'].value_counts().get('Don\'t know', 0)
nr_rv = noreligion['v2517'].value_counts().get('Refused', 0)
nr_bv = noreligion['v2509'].value_counts().get('Blank', 0)

# Calculates Percentages
noreligion_count = nr_yv + nr_nv + nr_dkv + nr_rv + nr_bv

nr_percentages = [
    nr_yv / noreligion_count, 
    nr_nv / noreligion_count, 
    nr_dkv / noreligion_count, 
    nr_rv / noreligion_count,
    nr_bv / noreligion_count]

# Plotting Religious
plt.subplot(1,2,2)
bars2 = plt.bar(survey_responses, nr_percentages)
plt.ylabel("% of Total")
plt.title("Rule Violations By NON-Religious Group Members")
plt.bar_label(
    bars2,
    labels=[f"{x:.1%}" for x in nr_percentages],  
    padding=3, 
    fontsize=9 
)


plt.show()