import requests
import json

API = "https://pokeapi.co/api/v2/generation/generation-ii"
response = requests.get(API)
pokemon = response.json()



print(pokemon.keys())
#dict_keys(['abilities', 'id', 'main_region', 'moves', 'name', 'names', 'pokemon_species', 'types', 'version_groups'])
print(pokemon['pokemon_species'])

print(pokemon['name'])

print(pokemon['types'])

print(pokemon['moves'])

print(pokemon['main_region'])

print(pokemon['names'])


pokemon_names = json.dumps(pokemon['name'])
print(pokemon_names)

pokemon_region = json.dumps(pokemon['main_region'])
print(pokemon_region)



