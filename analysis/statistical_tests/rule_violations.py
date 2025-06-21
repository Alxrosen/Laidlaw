import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

#Read the csv file
df = pd.read_csv('/Users/alexrosen/Laidlaw/data/prison_survey.csv')
    
variables = df[['v2500',                            # Education
                'v2517',                            # Rule violations
                'v0029', 'v0030', 'v0031', 'v0032', 'v0033', 'v0034', 'v0035', #Race
                'v0018',                            #Latino / Hispanic
                'v0715',                            # Sentence Length
                'v0004',                            # Gender
                'v0013',                             # age
                'v0046',                            # U.S. born
                'v0058'                             #Marital Status
                ]]

#limit to Yes and No for educational group  --> TODO June 21st Is this correct??
df_statsbinary = variables[
    ((variables['v2517'] == 'Yes') |
    (variables['v2517'] == 'No'))]

#convert rule violation and category to 1 and 0
df_statsbinary['v2517'] = df_statsbinary['v2517'].apply(lambda v: 1 if v == 'Yes' else 0)

# Education to binary
print(df_statsbinary['v2500'].value_counts())
df_statsbinary['v2500'] = df_statsbinary['v2500'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2500'])
df_statsbinary['v2500'] = df_statsbinary['v2500'].apply(lambda v: 1 if v == 'Yes' else 0)

print(df_statsbinary['v2500'].value_counts())
df_statsbinary = df_statsbinary.rename(columns={
    'v2500': 'community_Education' 
})


# Term sentence --> approximately how many years they have been incarcerated
df_statsbinary['v0715'] = df_statsbinary['v0715'].apply(lambda v: int(v) if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v0715'])
df_statsbinary['v0715'] = df_statsbinary['v0715'].apply(lambda v: 2004 - v)
df_statsbinary = df_statsbinary.rename(columns={
    'v0715': 'Sentence Length' 
})

# convert gender to binary
df_statsbinary['v0004'] = df_statsbinary['v0004'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v0004'])
df_statsbinary['v0004'] = df_statsbinary['v0004'].apply(lambda v: 1 if v == 'Male' else 0) # 1 = Male, 0 = Female
df_statsbinary = df_statsbinary.rename(columns={
    'v0004': 'Male' 
})


# Age
df_statsbinary['v0013'] = df_statsbinary['v0013'].apply(lambda v: int(v) if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused' or
                                            v == 0)
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v0013'])
df_statsbinary = df_statsbinary.rename(columns={
    'v0013': 'Age' 
})

#convert race categories to binary
df_statsbinary['v0029'] = df_statsbinary['v0029'].apply(lambda v: 1 if v != 'Blank' else 0)
df_statsbinary['v0030'] = df_statsbinary['v0030'].apply(lambda v: 1 if v != 'Blank' else 0)
df_statsbinary['v0031'] = df_statsbinary['v0031'].apply(lambda v: 1 if v != 'Blank' else 0)
df_statsbinary['v0032'] = df_statsbinary['v0032'].apply(lambda v: 1 if v != 'Blank' else 0)
df_statsbinary['v0033'] = df_statsbinary['v0033'].apply(lambda v: 1 if v != 'Blank' else 0)
df_statsbinary['v0034'] = df_statsbinary['v0034'].apply(lambda v: 1 if v != 'Blank' else 0)
df_statsbinary['v0035'] = df_statsbinary['v0035'].apply(lambda v: 1 if v != 'Blank' else 0)
df_statsbinary = df_statsbinary.rename(columns={
    'v0029': 'race_White',
    'v0030': 'race_Black',
    'v0031': 'race_American Indian Or Alaskan Native',
    'v0032': 'race_Asian',
    'v0033': 'race_Hawaiian Or Pacific Islander',
    'v0034': 'race_Other',
    'v0035': 'race_Unknown'
})

#convert hispanic categories to binary
df_statsbinary['v0018'] = df_statsbinary['v0018'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v0018'])
df_statsbinary['v0018'] = df_statsbinary['v0018'].apply(lambda v: 0 if v == 'No' else 1)
df_statsbinary = df_statsbinary.rename(columns={
    'v0018': 'Hispanic'
})

#convert U.S. Born categories to binary
df_statsbinary['v0046'] = df_statsbinary['v0046'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v0046'])
df_statsbinary['v0046'] = df_statsbinary['v0046'].apply(lambda v: 1 if v == 'United States' else 0)
df_statsbinary = df_statsbinary.rename(columns={
    'v0046': 'U.S. Born'
})

#convert Marital Status categories to binary
df_statsbinary['v0058'] = df_statsbinary['v0058'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v0058'])
marital_dummies = pd.get_dummies(df_statsbinary['v0058'], prefix='marital', dtype=int)
df_statsbinary = pd.concat([df_statsbinary, marital_dummies], axis=1)
df_statsbinary = df_statsbinary.drop('v0058', axis=1)


# drops rule violations column
output = df_statsbinary['v2517']
inputs = df_statsbinary.drop(['v2517'], axis = 1)

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