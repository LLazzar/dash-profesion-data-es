import pandas as pd

# Read the Excel file
df_urls = pd.read_excel("urls.xlsx", header=0)
df_urls.set_index(df['Area'], inplace=True)

def get_urls():
    return df_urls

#example
#df_urls.loc['Espana']
#df_urls.loc['Espana']['Data Engineer']