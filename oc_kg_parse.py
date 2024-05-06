import requests
from bs4 import BeautifulSoup

url = 'https://oc.kg/'


response = requests.get(url=url, verify=False)
soup = BeautifulSoup(response.text, 'html.parser')

main = soup.find('div', {'id': 'main'})
main_wrapper_div = main.find('div', {'id': 'main_wrapper'})
bestsellers_div = main_wrapper_div.find('div', {'class': 'content', 'id': 'bestsellers'})


genre_films_list = []
for bestseller_div in bestsellers_div:
    genre_film = bestseller_div.section.div.find('div', {'class': 'sectionheader'})
    genre_film_name = genre_film.a.get_text()
    genre_films_list.append(genre_film_name)

films_list = []
for films in bestsellers_div:
    
    film_name = bestsellers_div.section.div.find('div', {'class': 'item'}).get_text()
    films_list.append(film_name)

print(films_list)
print(genre_films_list)
