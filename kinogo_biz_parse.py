import requests
from bs4 import BeautifulSoup

def get_film_list():
    url = 'https://kinogo.biz/'

    response = requests.get(url=url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')

    content = soup.find('div', {'class': 'content'})
    dle_contents = content.find('div', {'id': 'dle-content'})

    film_list = []

    for film_detail in dle_contents.children:
        if film_detail.name == 'div':
            film_header = film_detail.find('div', {'class': 'shortstory__header'})
            film_url = film_header.find('a') if film_header else None
            if film_url:
                film_url_href = film_url.get('href')
            else:
                film_url_href = ""

            film_name = film_detail.find('div', {'class': 'shortstory__header'})
            film_poster = film_detail.find('div', {'class': 'shortstory__poster'})
            film_info = film_detail.find('div', {'class': 'shortstory__info-wrapper'})
            film_description = film_detail.find('div', {'class': 'excerpt'})

            film_name_text = film_name.h2.get_text(strip=True) if film_name else ""
            film_info_text = film_info.get_text(strip=True) if film_info else ""
            film_description_text = film_description.get_text(strip=True) if film_description else ""

            if film_poster and film_poster.img and film_poster.img.get('src') != '/templates/Kinogo/images/clear-shortstory.gif':
                film_poster_src = film_poster.img.get('src')
            else:
                film_poster_src = "No poster available"

            film_list.append({
                'url': film_url_href,
                'name': film_name_text,
                'info': film_info_text,
                'description': film_description_text,
                'poster': film_poster_src
            })

            print(
                film_url_href,
                film_name_text,
                film_info_text,
                film_description_text,
                film_poster_src
            )
    return film_list


text = get_film_list()
