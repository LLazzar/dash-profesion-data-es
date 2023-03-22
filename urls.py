import pandas as pd

# Read the Excel file
df_urls = pd.read_excel("urls.xlsx", header=0)
df_urls.set_index(df_urls['Area'], inplace=True)

#example
df_urls.loc['Espana']
df_urls.loc['Espana']['Data Engineer']

