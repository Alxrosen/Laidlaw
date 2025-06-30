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
                'v2540',                            # disobeying violations
                'v2541',                            # count disobeying violations
                'v0037', 'v0038', 'v0039', 'v0040', 'v0041', # Race (Allocated)
                'v0042',                            # Race - Other (commented out)
                'v0043',                            # Race - Unknown (commented out)
                'v0018',                            # Latino / Hispanic
                'v0715',                            # Sentence Length
                'v0717',                            # Sentence Length Changed to 2004 Flag
                'v0004',                            # Gender
                'v0013',                            # age
                'v0046',                            # U.S. born
                'v0058',                            # Marital Status
                #'v1056'                            # State
                #'v2984',                            # Facility ID
                #'v0718'                            # Age when Sentenced
                'v1198'                             # Age at first arrest
                ]]

df_statsbinary = variables[
    ((variables['v2540'] == 'Yes') |
    (variables['v2540'] == 'No'))]

# disobeying rule violation count
df_statsbinary['v2540'] = df_statsbinary['v2540'].apply(lambda v: 1 if v == 'Yes' else 0)
df_statsbinary['v2541'] = np.where(
    df_statsbinary['v2540'] == 0,  
    0,                       
    df_statsbinary['v2541']      
)
print(df_statsbinary['v2541'].value_counts())
df_statsbinary['v2541'] = df_statsbinary['v2541'].apply(lambda v: int(v) if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2541'])


# Education to binary
df_statsbinary['v2500'] = df_statsbinary['v2500'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2500'])
df_statsbinary['v2500'] = df_statsbinary['v2500'].apply(lambda v: 1 if v == 'Yes' else 0)
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
df_statsbinary['v2514'] = df_statsbinary['v2514'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2514'])
df_statsbinary['v2514'] = df_statsbinary['v2514'].apply(lambda v: 1 if v == 'Yes' else 0)
df_statsbinary = df_statsbinary.rename(columns={
    'v2514': 'community_Child Rearing' 
})

# Inmate-Assistance to binary
df_statsbinary['v2511'] = df_statsbinary['v2511'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2511'])
df_statsbinary['v2511'] = df_statsbinary['v2511'].apply(lambda v: 1 if v == 'Yes' else 0)
df_statsbinary = df_statsbinary.rename(columns={
    'v2511': 'community_Inmate Assistance' 
})

# Life Skills to binary
df_statsbinary['v2515'] = df_statsbinary['v2515'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2515'])
df_statsbinary['v2515'] = df_statsbinary['v2515'].apply(lambda v: 1 if v == 'Yes' else 0)
df_statsbinary = df_statsbinary.rename(columns={
    'v2515': 'community_Life Skills' 
})

# Pre-Release Programs to binary
df_statsbinary['v2516'] = df_statsbinary['v2516'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2516'])
df_statsbinary['v2516'] = df_statsbinary['v2516'].apply(lambda v: 1 if v == 'Yes' else 0)
df_statsbinary = df_statsbinary.rename(columns={
    'v2516': 'community_Pre-Release' 
})

# Race/Ethnicity to binary
df_statsbinary['v2510'] = df_statsbinary['v2510'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2510'])
df_statsbinary['v2510'] = df_statsbinary['v2510'].apply(lambda v: 1 if v == 'Yes' else 0)
df_statsbinary = df_statsbinary.rename(columns={
    'v2510': 'community_Race/Ethnicity' 
})

# Religious to binary
df_statsbinary['v2509'] = df_statsbinary['v2509'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2509'])
df_statsbinary['v2509'] = df_statsbinary['v2509'].apply(lambda v: 1 if v == 'Yes' else 0)
df_statsbinary = df_statsbinary.rename(columns={
    'v2509': 'community_Religion'
})

# Self-Help to binary
df_statsbinary['v2512'] = df_statsbinary['v2512'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2512'])
df_statsbinary['v2512'] = df_statsbinary['v2512'].apply(lambda v: 1 if v == 'Yes' else 0)
df_statsbinary = df_statsbinary.rename(columns={
    'v2512': 'community_Self-Help' 
})

# Vocational to binary
df_statsbinary['v2513'] = df_statsbinary['v2513'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v2513'])
df_statsbinary['v2513'] = df_statsbinary['v2513'].apply(lambda v: 1 if v == 'Yes' else 0)
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
'''
Here, I rely on the edited data from the v0717 flag
'''
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
    'v0715': 'control_Sentence length' 
})


# convert sex to binary
'''
Checks if they are Male for regression
'''
df_statsbinary['v0004'] = df_statsbinary['v0004'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v0004'])
df_statsbinary['v0004'] = df_statsbinary['v0004'].apply(lambda v: 1 if v == 'Male' else 0) # 1 = Male, 0 = Female
df_statsbinary = df_statsbinary.rename(columns={
    'v0004': 'control_Sex (Male)' 
})


# Age
'''
Dropped people who had "0" age
'''
df_statsbinary['v0013'] = df_statsbinary['v0013'].apply(lambda v: int(v) if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused' or
                                            v == 0)
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v0013'])
df_statsbinary = df_statsbinary.rename(columns={
    'v0013': 'control_Age' 
})

# Convert race categories to binary (allocated race columns)
'''
Uses allocated race instead of self-described. Then, drops the responses for the 27 individuals for whom all race values are Blank.
Used the largest category, White, as the comparison case. 
'''
race_cols = ['v0037', 'v0038', 'v0039', 'v0040', 'v0041', 'v0042', 'v0043']
df_statsbinary = df_statsbinary[df_statsbinary[race_cols].apply(lambda row: not all(val == 'Blank' for val in row), axis=1)]
for column in race_cols:
    df_statsbinary[column] = df_statsbinary[column].apply(lambda v: 1 if v != 'Blank' else 0)
df_statsbinary = df_statsbinary.rename(columns={
    'v0037': 'control_race_White',
    'v0038': 'control_race_Black',
    'v0039': 'control_race_American Indian Or Alaskan Native',
    'v0040': 'control_race_Asian',
    'v0041': 'control_race_Hawaiian Or Pacific Islander',
    'v0042': 'control_race_Other',     # Commented out: Other race   
    'v0043': 'control_race_Unknown'   # Commented out: Unknown race
})
df_statsbinary = df_statsbinary.drop(['control_race_White'], axis = 1)

#convert hispanic categories to binary
df_statsbinary['v0018'] = df_statsbinary['v0018'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v0018'])
df_statsbinary['v0018'] = df_statsbinary['v0018'].apply(lambda v: 0 if v == 'No' else 1)
df_statsbinary = df_statsbinary.rename(columns={
    'v0018': 'control_Hispanic'
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
    'v0046': 'control_U.S. Born'
})

#convert Marital Status categories to binary
'''
Chose to drop control_marital_Married to set that as the baseline group (having removed Blank, DK, and Refused) 
'''
df_statsbinary['v0058'] = df_statsbinary['v0058'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v0058'])
marital_dummies = pd.get_dummies(df_statsbinary['v0058'], prefix='control_marital', drop_first = False, dtype=int) #Instead, dropping manually below
df_statsbinary = pd.concat([df_statsbinary, marital_dummies], axis=1)
df_statsbinary = df_statsbinary.drop('v0058', axis=1)
df_statsbinary = df_statsbinary.drop('control_marital_Married', axis=1)

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
'''
Note: This data only includes State Facilities. Federal are in the other data set. Chose to drop first because data is anonymized and first has a large sample size
'''
'''
df_statsbinary['v2984'] = df_statsbinary['v2984'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary['v2984'] = df_statsbinary['v2984'].apply(lambda v: v if v < 401 else None)  # optional, supposed to remove federal (but none)
df_statsbinary = df_statsbinary.dropna(subset=['v2984'])
facility_dummies = pd.get_dummies(df_statsbinary['v2984'], prefix='control_facilityID', drop_first=True, dtype=int) 
df_statsbinary = pd.concat([df_statsbinary, facility_dummies], axis=1)
df_statsbinary = df_statsbinary.drop('v2984', axis=1) # Get's rid of the column still with unsorted info (which is now in dummy columns)
# df_statsbinary = df_statsbinary.drop('control_facilityID_', axis=1)
'''
# Age when Sentenced
'''
Removed because not enough people: <100
'''
# print(df_statsbinary['v0718'].value_counts())
# df_statsbinary['v0718'] = df_statsbinary['v0718'].apply(lambda v: int(v) if not \
#                                             (v == 'Blank' or
#                                             v == 'Don\'t know' or
#                                             v == 'Refused')
#                                             else None)
# df_statsbinary = df_statsbinary.dropna(subset=['v0718'])
# print(df_statsbinary['v0718'].value_counts())
# df_statsbinary = df_statsbinary.rename(columns={
#     'v0718': 'control_Age when sentenced' 
# })

# Age at first arrest
df_statsbinary['v1198'] = df_statsbinary['v1198'].apply(lambda v: int(v) if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v1198'])
df_statsbinary = df_statsbinary.rename(columns={
    'v1198': 'control_Age at first arrest'
})

# drops rule violations column and incarceration flag
output = df_statsbinary['v2541']
inputs = df_statsbinary.drop(['v2540', 'v2541', 'v0717'], axis = 1)    

# Show odds values as well
pd.set_option('display.max_rows', None)    # Show all rows
log_reg = sm.ZeroInflatedNegativeBinomialP(output, inputs).fit()
print(log_reg.summary())
odds_ratios = np.exp(log_reg.params)
print("\n\n ========== Odds ========== \n\n", odds_ratios)

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