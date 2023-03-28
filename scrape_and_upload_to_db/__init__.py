import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)


import urls
import store
import load_to_database

temp=store.fill_job_count(urls.df_urls.loc['Espana'])
load_to_database.uploadDict(temp)


import config
config.settings

temp['id']="2023-04-30"