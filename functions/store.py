from functions import scrape
import datetime

def fill_job_count(df_urls_count_area): #store in dictionary values gotten by scraping
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d")
    job_count = {
    "id": datetime.datetime.now().strftime("%Y-%m-%d"),
    "data_engineer": scrape.getNumberJobs(df_urls_count_area['Data Engineer']),
    "data_scientist": scrape.getNumberJobs(df_urls_count_area['Data Scientist']),
    "data_analyst": scrape.getNumberJobs(df_urls_count_area['Data Analyst']),
    "business_analyst": scrape.getNumberJobs(df_urls_count_area['Business Analyst']),
    "area": df_urls_count_area['Area']
    }
    return job_count

def fill_job_salary(df_urls_salary_job): #store in dictionary values gotten by scraping
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d")
    job_count = {
    "id": datetime.datetime.now().strftime("%Y-%m-%d"),
    "median": scrape.getMedianSalary(df_urls_salary_job['urls']),
    "q1": scrape.getLowerQuartileSalary(df_urls_salary_job['urls']),
    "q3": scrape.getUpperQuartileSalary(df_urls_salary_job['urls']),
    "job": df_urls_salary_job['job']
    }
    return job_count