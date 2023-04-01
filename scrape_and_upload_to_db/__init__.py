import datetime
import logging
import azure.functions as func

from functions import urls
from functions import store
from functions import load_to_database


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    #scrape and upload a json containing job counts for each area to database
    for index, row in urls.df_urls_count.iterrows():
        temp=store.fill_job_count(row) #temp is the directionary containing data relative to an area
        load_to_database.uploadDict(temp, "glassdoor_count") #upload dict temp to database and the right container
    
    #scrape and upload a json containing salary figures for each job to database
    for index, row in urls.df_urls_salary.iterrows():
        temp2=store.fill_job_salary(row) #temp is the directionary containing data relative to an area
        load_to_database.uploadDict(temp2, "glassdoor_salary") #upload dict temp to database and the right container




