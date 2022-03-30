import requests
from pprint import pprint

response = requests.get("http://hp-api.herokuapp.com/api/characters")
data = response.json()
# pprint(set([char.get('species') for char in data]))
# pprint([char for char in data if char.get('species') == 'dragon'])
print('Co chciał/chciała byś zobaczyc? ')
print('1. Postacie z okreslonym kolorem oczy? ')
print('2. Postacie z okreslonym "species"? ')

option = input('Podaj swój wybór: ')
if option == '1':
    eye_color = input("Podaj kolor oczu: ")
    pprint([char for char in data if char.get('eyeColou1r') == eye_color])
elif option == '2':
    species = input("Podaj species: ")
    pprint([char for char in data if char.get('species') == species])
