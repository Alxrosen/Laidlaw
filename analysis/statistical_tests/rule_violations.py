import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

#Read the csv file
df = pd.read_csv('/Users/alexrosen/Laidlaw/data/prison_survey.csv')
    
variables = df[['v2500',                            # Education
                #'v2508',                           # GED Acquisition --> High Multicollinearity
                'v2511',                            # Inmate Assistance
                'v2514',                            # Child Rearing
                'v2515',                            # Life Skills       
                'v2516',                            # Pre-Release  
                'v2510',                            # Race/Ethnicity
                'v2509',                            # Religious
                'v2512',                            # Self-Help
                'v2513',                            # Vocational (Ever, NOT currently)
                'v2517',                            # Rule violations
                'v0029', 'v0030', 'v0031', 'v0032', 'v0033', 'v0034', 'v0035', #Race
                'v0018',                            # Latino / Hispanic
                'v0715',                            # Sentence Length
                'v0717',                            # Sentence Length Changed to 2004 Flag
                'v0004',                            # Gender
                'v0013',                            # age
                'v0046',                            # U.S. born
                'v0058',                            # Marital Status
                #'v1056'                            # State
                'v2984'                             # Facility ID
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


# GED Acquisition to binary
'''
This is a good control against community_Education because this 
includes those who succeeded both with individual and community 
study, meaning that if we control for community studying we can 
show whether community studying or independend studying is better. 

However, cannot add because of high Multicorrinearity
'''
'''
print(df_statsbinary['v2508'].value_counts())
df_statsbinary['v2508'] = df_statsbinary['v2508'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2508'])
df_statsbinary['v2508'] = df_statsbinary['v2508'].apply(lambda v: 1 if v == 'Yes' else 0)
print(df_statsbinary['v2508'].value_counts())
df_statsbinary = df_statsbinary.rename(columns={
    'v2508': 'control_GED Acquisition' 
})
'''

# Child Rearing to binary
print(df_statsbinary['v2514'].value_counts())
df_statsbinary['v2514'] = df_statsbinary['v2514'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2514'])
df_statsbinary['v2514'] = df_statsbinary['v2514'].apply(lambda v: 1 if v == 'Yes' else 0)
print(df_statsbinary['v2514'].value_counts())
df_statsbinary = df_statsbinary.rename(columns={
    'v2514': 'community_Child Rearing' 
})

# Inmate-Assistance to binary
print(df_statsbinary['v2511'].value_counts())
df_statsbinary['v2511'] = df_statsbinary['v2511'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2511'])
df_statsbinary['v2511'] = df_statsbinary['v2511'].apply(lambda v: 1 if v == 'Yes' else 0)
print(df_statsbinary['v2511'].value_counts())
df_statsbinary = df_statsbinary.rename(columns={
    'v2511': 'community_Inmate Assistance' 
})

# Life Skills to binary
print(df_statsbinary['v2515'].value_counts())
df_statsbinary['v2515'] = df_statsbinary['v2515'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2515'])
df_statsbinary['v2515'] = df_statsbinary['v2515'].apply(lambda v: 1 if v == 'Yes' else 0)
print(df_statsbinary['v2515'].value_counts())
df_statsbinary = df_statsbinary.rename(columns={
    'v2515': 'community_Life Skills' 
})

# Pre-Release Programs to binary
print(df_statsbinary['v2516'].value_counts())
df_statsbinary['v2516'] = df_statsbinary['v2516'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2516'])
df_statsbinary['v2516'] = df_statsbinary['v2516'].apply(lambda v: 1 if v == 'Yes' else 0)
print(df_statsbinary['v2516'].value_counts())
df_statsbinary = df_statsbinary.rename(columns={
    'v2516': 'community_Pre-Release' 
})

# Race/Ethnicity to binary
print(df_statsbinary['v2510'].value_counts())
df_statsbinary['v2510'] = df_statsbinary['v2510'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2510'])
df_statsbinary['v2510'] = df_statsbinary['v2510'].apply(lambda v: 1 if v == 'Yes' else 0)
print(df_statsbinary['v2510'].value_counts())
df_statsbinary = df_statsbinary.rename(columns={
    'v2510': 'community_Race/Ethnicity' 
})

# Religious to binary
print(df_statsbinary['v2509'].value_counts())
df_statsbinary['v2509'] = df_statsbinary['v2509'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2509'])
df_statsbinary['v2509'] = df_statsbinary['v2509'].apply(lambda v: 1 if v == 'Yes' else 0)
print(df_statsbinary['v2509'].value_counts())
df_statsbinary = df_statsbinary.rename(columns={
    'v2509': 'community_Religion'
})

# Self-Help to binary
print(df_statsbinary['v2512'].value_counts())
df_statsbinary['v2512'] = df_statsbinary['v2512'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2512'])
df_statsbinary['v2512'] = df_statsbinary['v2512'].apply(lambda v: 1 if v == 'Yes' else 0)
print(df_statsbinary['v2512'].value_counts())
df_statsbinary = df_statsbinary.rename(columns={
    'v2512': 'community_Self-Help' 
})

# Vocational to binary
print(df_statsbinary['v2513'].value_counts())
df_statsbinary['v2513'] = df_statsbinary['v2513'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2513'])
df_statsbinary['v2513'] = df_statsbinary['v2513'].apply(lambda v: 1 if v == 'Yes' else 0)
print(df_statsbinary['v2513'].value_counts())
df_statsbinary = df_statsbinary.rename(columns={
    'v2513': 'community_Vocational' 
})

# Template to binary
'''
print(df_statsbinary['v0000'].value_counts())
df_statsbinary['v0000'] = df_statsbinary['v0000'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v0000'])
df_statsbinary['v0000'] = df_statsbinary['v0000'].apply(lambda v: 1 if v == 'Yes' else 0)
print(df_statsbinary['v0000'].value_counts())
df_statsbinary = df_statsbinary.rename(columns={
    'v0000': 'community_Template' 
})
'''

# Sentence sentence --> approximately how many years they have been incarcerated
df_statsbinary['v0717'] = df_statsbinary['v0717'].apply(lambda v: 1 if v == "Year field changed to 2004" else 0)
df_statsbinary['v0715'] = np.where(
    df_statsbinary['v0717'] == 1,  
    2004,                       
    df_statsbinary['v0715']      
)
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

#convert State Residency during arrest categories to binary
'''
Creates multicollinearity (or dummy variable trap?)
df_statsbinary['v1056'] = df_statsbinary['v1056'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v1056'])
marital_dummies = pd.get_dummies(df_statsbinary['v1056'], prefix='state', dtype=int)
df_statsbinary = pd.concat([df_statsbinary, marital_dummies], axis=1)
df_statsbinary = df_statsbinary.drop('v1056', axis=1)
'''

# By-Facility Factor -- 
# '''
# Dropped Federal Facilities 
# 101 - 387 (State Facilities)
# 401 - 439 (Federal Facilities)
# '''
#Creates multicollinearity (or dummy variable trap?)
print(df_statsbinary['v2984'].value_counts())
df_statsbinary['v2984'] = df_statsbinary['v2984'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary['v2984'] = df_statsbinary['v2984'].apply(lambda v: v if v < 401 else None) 
df_statsbinary = df_statsbinary.dropna(subset=['v2984'])
marital_dummies = pd.get_dummies(df_statsbinary['v2984'], prefix='facility', drop_first=True, dtype=int)
df_statsbinary = pd.concat([df_statsbinary, marital_dummies], axis=1)
print(df_statsbinary['v2984'].value_counts())
df_statsbinary = df_statsbinary.drop('v2984', axis=1) # Get's rid of the column still with unsorted info (which is now in dummy columns)



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