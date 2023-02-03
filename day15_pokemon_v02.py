# example 115p pokemon ver01


# find and add def section
def find_add_insert_data(pokemon, hp):
    """
    Finding itself space by health percent and add an new data in Pokémon dict list
    :param pokemon: pokemon name
    :param hp: health percent
    :return: list of friends contact and number
    """
    findPos = -1
    for i in range(len(pokemons)):
        pair = pokemon[i]
        if hp >= list(pair.values())[0]:
            findPos = 1
            break

    if findPos == -1:
        findPos = len(pokemon)

    insert_data(findPos, {pokemon, hp})

def insert_data(idx, pokemon):
    if idx < 0 or idx > len(pokemons):
        print('Out of space')
        return
    pokemons.append(None)

    for i in range(len(pokemons)-1, idx, -1):
        pokemons[i] = pokemons[i-1]
        pokemons[i-1] = None

    pokemons[idx] = pokemon

# making tuple list for name and number of contact
pokemons = dict[{'Greninja' : 5400}, {'Mimikyu' : 3266}, {'Umbreon' : 197}, {'Pikachu' : 51}, {'Charizard' : 30}]
# main section
if __name__ == "__main__":

    while True:
        name = input('Please enter your new pokemon: -->')
        hp = int(input(f"Please enter {name}'s hp -->"))
        find_add_insert_data(name, hp)
        print(pokemons)