import requests

nombre="pikachu"
url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"

response = requests.get(url)


data = response.json()


nombre_pokemon = data['name'].capitalize()
id_pokemon = data['id']

print(nombre_pokemon) 