import requests
from bs4 import BeautifulSoup
from functions import string_transf

def getNumberJobs(url): #scrape function
    url = url
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content,'html.parser')
    return soup.find('h1', {'class': 'hideHH css-zga872 e15r6eig0'}).text.split()[0]

def getMedianSalary(url): #scrape function
    url = url
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content,'html.parser')
    return string_transf.convertM(soup.find('span', {'data-test': 'formatted-pay'}).text.split()[0])

def getLowerQuartileSalary(url): #scrape function
    url = url
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content,'html.parser')
    return string_transf.convertQ(soup.find_all('span', {'class': 'm-0 css-1b6bxoo'})[1].text)

def getUpperQuartileSalary(url): #scrape function
    url = url
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content,'html.parser')
    return string_transf.convertQ(soup.find_all('span', {'class': 'm-0 css-1b6bxoo'})[2].text)

