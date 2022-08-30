from pokemons import Pokemons

options = ["1","2","3"]
poke = Pokemons()
while True:
    print ("...Pokedex...")
    print ("1. Pokemon list")
    print ("2. Search Pokemon")
    print ("3. Exit")

    selection = str (input ("Select your option: "))

    if selection not in options:
        print ("Select a valid option, please")

    if selection == "1" :
        poke.show_list()

    if selection == "2":
        poke_srch = input ("Write the name of the pokemon: ").lower ()
        poke.search_pokemon (poke_srch)


    if selection == "3" :
        break
