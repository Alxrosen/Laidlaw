import arviz as az
import bambi as bmb
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
                'v2984',                            # Facility ID
                #'v1056',                            # State Residence at Arrest
                #'v0718'                            # Age when Sentenced
                'v1198'                             # Age at first arrest
                ]]

df_statsbinary = variables[
    ((variables['v2517'] == 'Yes') |
    (variables['v2517'] == 'No'))]

#convert rule violation and category to 1 and 0
df_statsbinary['v2517'] = df_statsbinary['v2517'].apply(lambda v: 1 if v == 'Yes' else 0)

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
    'v2514': 'community_Child_Rearing' 
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
    'v2511': 'community_Inmate_Assistance' 
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
    'v2515': 'community_Life_Skills' 
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
    'v2516': 'community_Pre_Release' 
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
    'v2510': 'community_Race_Ethnicity' 
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
    'v2512': 'community_Self_Help' 
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
    'v0715': 'control_Sentence_Length' 
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
    'v0004': 'control_Sex_Male' 
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
    'v0039': 'control_race_American_Indian_Or_Alaskan_Native',
    'v0040': 'control_race_Asian',
    'v0041': 'control_race_Hawaiian_Or_Pacific_Islander',
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
    'v0046': 'control_US_Born'
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
df_statsbinary['v0058'] = df_statsbinary['v0058'].str.replace(' ', '_')
df_statsbinary['v0058'] = df_statsbinary['v0058'].str.replace('(Not_because_of_incarceration)', '')
marital_dummies = pd.get_dummies(df_statsbinary['v0058'], prefix='control_marital', drop_first = False, dtype=int) #Instead, dropping manually below
df_statsbinary = pd.concat([df_statsbinary, marital_dummies], axis=1)
df_statsbinary = df_statsbinary.drop('v0058', axis=1)
df_statsbinary = df_statsbinary.drop('control_marital_Married', axis=1)

#convert State Residency during arrest categories to binary
'''
Creates multicollinearity (or dummy variable trap?)
'''
'''
df_statsbinary['v1056'] = df_statsbinary['v1056'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v1056'])
state_dummies = pd.get_dummies(df_statsbinary['v1056'], prefix='state', drop_first=True, dtype=int)
df_statsbinary = pd.concat([df_statsbinary, state_dummies], axis=1)
df_statsbinary = df_statsbinary.drop('v1056', axis=1)
'''

# Facility Size Variable
#df_statsbinary['facility_size'] = df_statsbinary['v2984'].apply(lambda v: (df_statsbinary['v2984'] == v).sum())

# Residence
#V1056


# Facility Location
'''
Sets the facility location as where the majority of the incarcerated individuals there had residence prior to their arrest. Collinearity with Facility ID
'''
'''
df_statsbinary['v1056'] = df_statsbinary['v1056'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary = df_statsbinary.dropna(subset=['v1056'])
df_statsbinary['facility_location'] = df_statsbinary['v2984'].apply(
    lambda facility: df_statsbinary[df_statsbinary['v2984'] == facility]['v1056'].mode()[0]
)
location_dummies = pd.get_dummies(df_statsbinary['facility_location'], prefix='control_facility_location', drop_first = False, dtype=int) #Instead, dropping manually below
df_statsbinary = pd.concat([df_statsbinary, location_dummies], axis=1)
df_statsbinary = df_statsbinary.drop('v1056', axis=1)
df_statsbinary = df_statsbinary.drop('facility_location', axis=1)
df_statsbinary = df_statsbinary.drop('control_facility_location_Texas', axis=1)
'''

# By-Facility Factor -- 
'''
Note: This data only includes State Facilities. Federal are in the other data set. Chose to drop first because data is anonymized and first has a large sample size
'''
df_statsbinary['v2984'] = df_statsbinary['v2984'].apply(lambda v: v if not \
                                            (v == 'Blank' or
                                            v == 'Don\'t know' or
                                            v == 'Refused')
                                            else None)
df_statsbinary['v2984'] = df_statsbinary['v2984'].apply(lambda v: v if v < 401 else None)  # optional, supposed to remove federal (but none)
df_statsbinary = df_statsbinary.dropna(subset=['v2984'])
#NOTE removing dummy variables for passing to bambi as cluster
#facility_dummies = pd.get_dummies(df_statsbinary['v2984'], prefix='control_facilityID', drop_first=True, dtype=int) 
#df_statsbinary = pd.concat([df_statsbinary, facility_dummies], axis=1)
#df_statsbinary = df_statsbinary.drop('v2984', axis=1) # Get's rid of the column still with unsorted info (which is now in dummy columns)
# df_statsbinary = df_statsbinary.drop('control_facilityID_', axis=1)

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
    'v1198': 'control_Age_at_first_arrest'
})

def run(df_statsbinary):
    # drops rule violations column and incarceration flag
    output = df_statsbinary['v2517']
    inputs = df_statsbinary.drop(['v2517', 'v0717', 'v2984'], axis = 1)
    fixed_effects = inputs.columns.tolist() 
    print("\n\n\n", fixed_effects)
    inputs_li = ' + '.join(fixed_effects)
    print("\n\n\n", inputs_li)

    # Create the mixed effects model with facility_id as random intercept
    model = bmb.Model(f"v2517 ~ {inputs_li} + (1|v2984)", 
        data=df_statsbinary, 
        family="bernoulli", 
        link="logit")

    # Fit the model
    fitted = model.fit(draws=2000, tune=1000, chains=4, cores=1)

    # Get summary (includes credible intervals instead of p-values)
    print(az.summary(fitted))

    # Calculate odds ratios from posterior samples
    posterior = fitted.posterior

    print("\n\n ========== Odds Ratios (Mean and 95% CI) ========== \n")
    for param in fixed_effects:
        if param in posterior.data_vars:
            samples = posterior[param].values.flatten()
            odds_ratio_samples = np.exp(samples)
            
            mean_or = np.mean(odds_ratio_samples)
            ci_lower = np.percentile(odds_ratio_samples, 2.5)
            ci_upper = np.percentile(odds_ratio_samples, 97.5)
            
            print(f"{param}: {mean_or:.3f} (95% CI: {ci_lower:.3f} - {ci_upper:.3f})")

if __name__ == "__main__":
    run(df_statsbinary)