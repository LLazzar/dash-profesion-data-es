import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.linkedin.com/jobs/search?keywords=data engineer&location=España&geoId=105646813&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
response = requests.get(url)
print(response)

soup = BeautifulSoup(response.content,'html.parser')

job_count = soup.find('span', {'class': 'results-context-header__job-count'}).text