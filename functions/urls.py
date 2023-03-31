import pandas as pd

# Read the Excel file of urls to get job counts
df_urls_count = pd.read_excel("urls/urls_count.xlsx", header=0)
df_urls_count.set_index(df_urls_count['Area'], inplace=True)

#example
df_urls_count.loc['España'] #gives link for area 'Espana'
df_urls_count.loc['España']['Data Engineer']
df_urls_count.loc['España']['Area']

# Read the Excel file of urls to get salaries figures
df_urls_salary = pd.read_excel("urls/urls_salary.xlsx", header=0)
df_urls_salary.set_index(df_urls_salary['job'], inplace=True)

#example
df_urls_salary.loc['Data Engineer'] #gives link for job 'Data engineer'
df_urls_salary.loc['Data Engineer']['urls']
df_urls_salary.loc['Data Engineer']['job']

