import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

#Read the csv file
df = pd.read_csv('/Users/alexrosen/Laidlaw/data/prison_survey.csv')
    
education = df[['v2500',                            # Category
                'v2517',                            # Rule violations
                'v0029', 'v0030', 'v0031', 'v0032', 'v0033', 'v0034', 'v0035', #Race
                'v0018',                            #Latino / Hispanic
                'v0715',                            # Sentence Length
                'v0004',                            # Gender
                'v0013'                             # age
                ]]

#limit to Yes and No for educational group
edubinary = education[
    ((education['v2500'] == 'Yes') |
    (education['v2500'] == 'No')) &
    ((education['v2517'] == 'Yes') |
    (education['v2517'] == 'No'))]

#convert rule violation and category to 1 and 0
edubinary['v2500'] = edubinary['v2500'].apply(lambda v: 1 if v == 'Yes' else 0)
edubinary['v2517'] = edubinary['v2517'].apply(lambda v: 1 if v == 'Yes' else 0)

# Term sentence --> approximately how many years they have been incarcerated
edubinary['v0715'] = edubinary['v0715'].apply(lambda v: int(v) if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
edubinary = edubinary.dropna(subset=['v0715'])
edubinary['v0715'] = edubinary['v0715'].apply(lambda v: 2004 - v)

# convert gender to binary
edubinary['v0004'] = edubinary['v0004'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
edubinary = edubinary.dropna(subset=['v0004'])
edubinary['v0004'] = edubinary['v0004'].apply(lambda v: 1 if v == 'Male' else 0) # 1 = Male, 0 = Female

# Age
edubinary['v0013'] = edubinary['v0013'].apply(lambda v: int(v) if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused' or
                                            v == 0)
                                            else None)
edubinary = edubinary.dropna(subset=['v0013'])


#convert race categories to binary
edubinary['v0029'] = edubinary['v0029'].apply(lambda v: 1 if v != 'Blank' else 0)
edubinary['v0030'] = edubinary['v0030'].apply(lambda v: 1 if v != 'Blank' else 0)
edubinary['v0031'] = edubinary['v0031'].apply(lambda v: 1 if v != 'Blank' else 0)
edubinary['v0032'] = edubinary['v0032'].apply(lambda v: 1 if v != 'Blank' else 0)
edubinary['v0033'] = edubinary['v0033'].apply(lambda v: 1 if v != 'Blank' else 0)
edubinary['v0034'] = edubinary['v0034'].apply(lambda v: 1 if v != 'Blank' else 0)
edubinary['v0035'] = edubinary['v0035'].apply(lambda v: 1 if v != 'Blank' else 0)

#convert hispanic categories to binary
edubinary['v0018'] = edubinary['v0018'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
edubinary = edubinary.dropna(subset=['v0018'])
edubinary['v0018'] = edubinary['v0018'].apply(lambda v: 0 if v == 'No' else 1)
print(edubinary['v0018'].value_counts())

# drops rule violations column
output = edubinary['v2517']
inputs = edubinary.drop(['v2517'], axis = 1)

log_reg = sm.Logit(output, inputs).fit()
print(log_reg.summary())


#print(df[df['v0715'].str.isnumeric().fillna(False)]['v0715'].value_counts().index.min()) #Debugging

'''
YEAR FIRST ADMITTED
'''

'''
Throw EVERYTHING in there, controls for each of these. The coef are independent so creates unique effect of each one

!!! Include sentence as well
!!! Criminal History

'''
'''
v2500 --> education



V0029       S1Q3C_1: RACE - WHITE
128
V0030       S1Q3C_2: RACE - BLACK
128
V0031       S1Q3C_3: RACE - AMERICAN INDIAN/ALASKAN NATIVE
128
V0032       S1Q3C_4: RACE - ASIAN
128
V0033       S1Q3C_5: RACE - HAWAIIAN/PACIFIC ISLANDER
129
V0034       S1Q3C_6: RACE - OTHER
129
V0035       RACE - NOT KNOWN
129

'''