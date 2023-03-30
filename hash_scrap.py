import requests
from bs4 import BeautifulSoup
import time

def scrap():
    hashtag = input("Ingrese un hashtag: ")
    url = f'https://www.instagram.com/explore/tags/{hashtag}/'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    # extract the number of posts for the hashtag
    description = soup.find('meta', attrs={'name': 'description'})['content']
    num_posts = description.split()[0]

    print(f'Número de posteos para el hashtag {hashtag}: {num_posts}')

    while True:
        user_input = input('Presione Enter para ingresar otro hashtag o escriba "salir" para terminar: ')
        if user_input.lower() == 'salir':
            print("\n" * 1)
            print("Toda persona debe decidir al menos una vez en la vida,\n si se lanza a triunfar arriesgándolo todo,\n o se sienta cómodamente en su balcón\n a disfrutar del desfile de los triunfadores.")      
            print("\n" * 1)
            print("Python Tool developed by Hernán Mendez. All rights reserved.")
            print("\n" * 1)
            time.sleep(5)
            break
        elif user_input == '':
            print("\n" * 1)  # Add some blank lines to clear the output
            scrap()
            break

scrap()