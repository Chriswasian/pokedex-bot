import requests
import json

def get_evolution(pokemon_name):
	url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name.lower()}"
	response = requests.get(url)
	if response.status_code == 200:
		data = response.json()
	evo_url = data['evolution_chain']['url']
	evo_response = requests.get(evo_url)
	evo_data = evo_response.json()

	chain = evo_data['chain']
	print(f"\n🔥 {pokemon_name.capitalize()} Evolution Chain:")
	print_chain(chain)

	return chain

def print_chain(chain, indent=0):
	name = chain['species']['name'].capitalize()
	if chain['evolves_to']:
		for evolution in chain['evolves_to']:
			detail = evolution['evolution_details'][0]
			level = detail.get('min_level')
			item = detail.get('item')
			trigger = detail.get('trigger', {}).get('name', '')

			if level:
				condition = f"level {level}"
			elif item:
				condition = f"{item['name'].replace('-', ' ').title()}"
			elif trigger == 'trade':
				condition = "trading"
			elif detail.get('min_happiness'):
				condition = "happiness"
			else:
				condition = "special condition"

			next_name = evolution['species']['name'].capitalize()
			print(f"{' ' * indent}{name} → {next_name} ({condition})")
			print_chain(evolution, indent + 1)
	else:
		print(f"{' ' * indent}{name} → final form")


def main():
	while True:
		pokemon_name = input("\nEnter a Pokémon name to see its evolution chain (or 'exit' to quit): ")
		if pokemon_name.lower() == 'exit':
			print("Goodbye!")
			break
		get_evolution(pokemon_name)

if __name__ == '__main__':
				main()