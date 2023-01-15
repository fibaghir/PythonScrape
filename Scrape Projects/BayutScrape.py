from bs4 import BeautifulSoup
import requests
from csv import writer
from time import sleep

url = 'https://www.bayut.com/to-rent/villas/dubai/?property_types=3&location_ids=5002&campaignId=29&adgroupId=18743&ad=1&gclid=CjwKCAiA2fmdBhBpEiwA4CcHzVXIwmZD6SzOvZs9QOLLSi61wULugUNFydQaEjqkzwVcC03s5MrNuRoCPCAQAvD_BwE'
user_agent = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/90.0.4430.212 Safari/537.36',
               'Accept-Language': 'en-US, en;q=0.5'})

r = requests.get(url,headers = user_agent)
soup = BeautifulSoup(r.text,'html.parser')

with open('Bayut.csv', 'w', encoding='utf8', newline='') as f:
     thewriter = writer(f)
     header = ['Title','Property_Type','Location','Price','Bedrooms','Bathrooms','Area']
     thewriter.writerow(header)

     data=[]

     for p in range(1,16):
        print(p)

        url = f'https://www.bayut.com/to-rent/villas/dubai/?page={p}/property_types=3&location_ids=5002&campaignId=29&adgroupId=18743&ad=1&gclid=CjwKCAiA2fmdBhBpEiwA4CcHzVXIwmZD6SzOvZs9QOLLSi61wULugUNFydQaEjqkzwVcC03s5MrNuRoCPCAQAvD_BwE'
        r =  requests.get(url,headers = user_agent)
        sleep(2)
        soup = BeautifulSoup(r.text,'html.parser')
        lists = soup.find_all('li', class_="ef447dde")

        for list in lists:

            title = list.find('h2', class_= "_7f17f34f").text
            type = list.find('div', class_= "_9a4e3964").text
            location = list.find('div', class_= "_7afabd84").text
            price = list.find('span', class_= "f343d9ce").text
            bedrooms = list.find('span', class_= "b6a29bc0").text
            bathrooms = list.find('span', class_= "b6a29bc0").text
            area = list.find('span', {"aria-label": "Area"}).text

            info = [title,type,location,price,bedrooms,bathrooms,area]
            thewriter.writerow(info)
    
    

        
    
    

    



