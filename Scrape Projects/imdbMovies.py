import requests
from bs4 import BeautifulSoup 
from csv import writer

source = requests.get('https://www.imdb.com/chart/top/')
source.raise_for_status()

soup = BeautifulSoup(source.text,'html.parser')
movies = soup.find('tbody',class_='lister-list').find_all('tr')
        
with open('imdb.csv', 'w', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['Rank','Name','Release Year','Rating']
        thewriter.writerow(header)

        for movie in movies: 
            name = movie.find('td',class_="titleColumn").a.text
            rank = movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
            year = movie.find('td',class_="titleColumn").span.text.strip("()")
            rating= movie.find('td',class_="ratingColumn imdbRating").strong.text
            
            info = [rank,name,year,rating]
            thewriter.writerow(info)
