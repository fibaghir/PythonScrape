from bs4 import BeautifulSoup
import requests
from time import sleep
from csv import writer

url = "https://dubai.dubizzle.com/motors/used-cars/"
user_agent = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/90.0.4430.212 Safari/537.36',
               'Accept-Language': 'en-US, en;q=0.5'})

sr =  requests.get(url,headers = user_agent)
soup = BeautifulSoup(sr.content,'html.parser')

with open('dubizzle.csv', 'w', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['Title','Manufacturer','Model','Price','Location','Mileage','Number_of_Doors','Color']
        thewriter.writerow(header)
        
        
        data= []

        for p in range(1,11):
            print(p)

            url = f"https://dubai.dubizzle.com/motors/used-cars/?page={p}"
            sr =  requests.get(url,headers = user_agent)
            sleep(3)
            soup = BeautifulSoup(sr.content,'html.parser')
            lists = soup.find_all('div',class_="sc-cmkc2d-0 dhbOk")

            for list in lists:

                title = list.find('h2', class_="sc-cmkc2d-10 iOynTy").text
                manufacturer = list.find('div', class_="sc-cmkc2d-7 sc-12jmuzh-1 iZrQA-D kwQHqe heading-text-1").text
                model = list.find('div', class_="sc-cmkc2d-7 sc-12jmuzh-1 iZrQA-D kwQHqe heading-text-2").text
                price = list.find('div', class_="sc-cmkc2d-7 sc-11jo8dj-4 iZrQA-D dMMLUo").text
                location = list.find('div', class_= "sc-cmkc2d-26 hRlQnb").text
                mileage = list.find('div',attrs= {"data-testid": "listing-kms"}).text
                year = list.find('div',attrs= {"data-testid": "listing-year"}).text
                doors = list.find('div',attrs= {"data-testid": "listing-doors"}).text
                color = list.find('div',attrs= {"data-testid": "listing-color"}).text


                info = [title,manufacturer,model,price,location,mileage,doors,color]
                thewriter.writerow(info)

                
    



