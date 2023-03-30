import datetime
import logging
import azure.functions as func

import urls
import store
import load_to_database


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    for index, row in urls.df_urls.iterrows():
        temp=store.fill_job_count(row) #temp is the directionary containing data relative to an area
        load_to_database.uploadDict(temp) #upload to database




