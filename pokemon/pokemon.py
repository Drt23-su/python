import requests

def obtener_info_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        nombre_pokemon = data['name'].capitalize()
        id_pokemon = data['id']
        tipos = [tipo['type']['name'] for tipo in data['types']]
        habilidades = [hab['ability']['name'] for hab in data['abilities']]
        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}

        print(f" Información del Pokémon: {nombre_pokemon}")
        print(f"ID: {id_pokemon}")
        print(f"Tipos: {', '.join(tipos)}")
        print(f"Habilidades: {', '.join(habilidades)}")
        print("\nEstadísticas base")
        for stat, value in stats.items():
            print(f"   - {stat.capitalize()}: {value}")

    else:
        print("Pokémon no encontrado. Verifica el nombre o número.")

if __name__=="__main__":
    nombre_pokemon = input("Ingresa el nombre o número del Pokémon: ")
    obtener_info_pokemon(nombre_pokemon)