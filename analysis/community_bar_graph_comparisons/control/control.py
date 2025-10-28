import pandas as pd
import matplotlib.pyplot as plt

#Read the csv file
df = pd.read_csv('/Users/alexrosen/Laidlaw/data/prison_survey.csv')

'''

V2517 --> S10Q13A: Since your admission [MOST RECENT ADMISSION DATE], have you been written up
or found guilty of breaking any of the prison rules?
'''

''' 
Changes to Template
Just checking one condidiont: rule violation rates overall
'''

survey_responses = ['Yes', 'No', 'Don\'t know','Refused', 'Blank']



# Gets the counts by each of the violation answer categories
yc_yv = df['v2517'].value_counts().get('Yes', 0)
yc_nv = df['v2517'].value_counts().get('No', 0)
yc_dkv = df['v2517'].value_counts().get('Don\'t know', 0)
yc_rv = df['v2517'].value_counts().get('Refused', 0)
yc_bv = df['v2517'].value_counts().get('Blank', 0)

# Calculates Percentages
yescategory_count = yc_yv + yc_nv + yc_dkv + yc_rv + yc_bv

yc_percentages = [
    yc_yv / yescategory_count, 
    yc_nv / yescategory_count, 
    yc_dkv / yescategory_count, 
    yc_rv / yescategory_count,
    yc_bv / yescategory_count]


# Plotting Category
plt.subplot(1,1,1)
bars1 = plt.bar(survey_responses, yc_percentages)
plt.ylabel("% of Total")
plt.title("Rule Violations Overall")
plt.bar_label(
    bars1,
    labels=[f"{x:.1%}" for x in yc_percentages],  
    padding=3, 
    fontsize=9 
)


plt.show()