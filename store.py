import scrape
import datetime

def fill_job_count(df_urls_Area): #store in dictionary values gotten by scraping
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d")
    job_count = {
    "id": datetime.datetime.now().strftime("%Y-%m-%d"),
    "data_engineer": scrape.getNumberJobs(df_urls_Area['Data Engineer']),
    "data_scientist": scrape.getNumberJobs(df_urls_Area['Data Scientist']),
    "data_analyst": scrape.getNumberJobs(df_urls_Area['Data Analyst']),
    "business_analyst": scrape.getNumberJobs(df_urls_Area['Business Analyst']),
    "area": df_urls_Area['Area']
    }
    return job_count

fill_job_count(a)
scrape.getNumberJobs(a['Business Analysst'])