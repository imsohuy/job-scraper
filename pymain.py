from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f"Filtering out {unfamiliar_skill}")

def find_job():
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span',class_='sim-posted').span.text
        if 'few' in published_date:
            company = job.find('h3',class_='joblist-comp-name').text.replace(' ','') #replace('to be replace','replace with')
            skills = job.find('span','srp-skills').text.replace(' ','') #.find('tag to find','filter')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company Name: {company.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info} \n")
                print(f"File Saved: {index}")

if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait*60)
