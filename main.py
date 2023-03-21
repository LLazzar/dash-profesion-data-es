import csv
import requests
from bs4 import BeautifulSoup

url_data_scientist_espana="https://www.glassdoor.com/Job/spain-data-scientist-jobs-SRCH_IL.0,5_IN219_KO6,20.htm?clickSource=searchBox"

def getNumberJobs(url):
    url = url
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content,'html.parser')
    return soup.find('h1', {'class': 'hideHH css-zga872 e15r6eig0'}).text.split()[0]

import datetime

now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d")

def fill_job_count(rowUrls)
    job_count = {
    "id": datetime.datetime.now().strftime("%Y-%m-%d"),
    "data_engineer": getNumberJobs(url_data_scientist_espana),
    "data_scientist": getNumberJobs(url_data_scientist_espana),
    "data_analyst": getNumberJobs(url_data_scientist_espana),
    "business_analyst": getNumberJobs(url_data_scientist_espana),
    "area": area
    }
    return job_count