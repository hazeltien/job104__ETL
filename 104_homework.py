import requests
from bs4 import BeautifulSoup
import json
import time
import random
import csv
import pandas as pd

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

url = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=15&asc=0&page=10&mode=s&jobsource=2018indexpoc&langFlag=0'

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

jobs = soup.find_all('article', class_='js-job-item')
linkList = []
nameList=[]
companyList=[]
contentList=[]

for job in jobs:
    time.sleep(random.randint(1, 50) / 10)
    link = 'https:'+job.select('a')[0]['href']
    linkList.append(link)
    name = job.select('a')[0].text
    nameList.append(name)
    company = job.select('a')[1].text
    companyList.append(company)
    content = job.find('p').text
    contentList.append(content)
    # print('https:'+link)
    # print(name)
    # print(company)
    # print(content)
    # print("================================")
df = pd.DataFrame({
    'Company': companyList,
    'Job Opening': nameList,
    'Job Content': contentList,
    'Job URL': linkList
})
df.to_csv('C:\\Users\\Hazel\\Desktop\\TFI101\\Python爬蟲\\104_ETL.csv',encoding='utf_8_sig')