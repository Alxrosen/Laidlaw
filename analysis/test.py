import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/alexrosen/Laidlaw/data/prison_survey.csv')

pd.set_option('display.max_rows', 15000)

pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)        # Don't wrap lines
pd.set_option('display.max_colwidth', 50)   # Limit column width

#for i, (column, value) in enumerate(list(df.iloc[0].items())[:2984]):
#    print(f"{i+1}. {column}: {value}")

rows, columns = df.shape
print(f"Rows: {rows}, Columns: {columns}")