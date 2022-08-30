import requests
import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Pokemons:
        #Class variables

    pokemon_Type = None
    pokemon_Habilities = None
    pokemon_names = []
    offset = 0
    p_results = {}
        #Class constructor
    def ___init__ (self):
        pass

    #List first 20 pokemons from the api
    def list_pokemon(offset):
        #Offset of the pokemon name list
        args = {'offset':offset} if offset else {}

        response = requests.get ('https://pokeapi.co/api/v2/pokemon/',params = args)
        #Check request success
        if response.status_code == 200:
            pokemon_list = response.json ()
            Pokemons.p_results = pokemon_list.get ('results',[])

            if Pokemons.p_results:
                for p in Pokemons.p_results:
                    Pokemons.pokemon_names.append (p['name'])

    # Search pokemon characteristics by its name
    def search_pokemon (self,pok_srch):
        Pokemons.list_pokemon (Pokemons.offset)
        #print ("Searching .......")
        url = "https://pokeapi.co/api/v2/pokemon/"+ pok_srch

        response2 = requests.get (url)
        print (response2.url)
        if response2.status_code == 200:
            ty = []
            st = []
            st_n = ['HP','Attack','Defense']
            pok_n = response2.json()
            print ("Name: ",pok_n['name'])
            #Get the type of the pokemon
            types = pok_n.get('types',[])

            for i in types:
                tp = i.get('type',[])
                ty.append (tp['name'])

            #Get pokemon basic stats
            stats = pok_n.get ('stats',[])
            for s in range (3):
                sta = stats[s]
                st.append(sta['base_stat'])

            print ("Type: ",end=" ")
            print (ty)

            #Show pokemon
            image_url = pok_n['sprites']['front_default']
            plt.subplot(131)

            #plt.bar(st_n, st "To show the stats with bars"


            plt.pie(st, labels=st_n,autopct=lambda p : '({:,.0f})'.format(p * sum(st)/100), startangle=140)
            plt.subplot(133)

            image = mpimg.imread (image_url)

            imgplot = plt.imshow(image)

            plt.suptitle ((pok_n['name']+"\n"+' '.join(ty)).upper())
            plt.show()

        else :
            print ("Error, pokemon not found ")




  # List pokemons name's
    def show_list (self):

        Pokemons.list_pokemon (Pokemons.offset)
        for pok_nam in Pokemons.pokemon_names:
            print (pok_nam)
        next = input ("¿Continue? [Y] [N/Select any other key]").lower()
        if next == 'y':
            Pokemons.pokemon_names.clear ()
            Pokemons.offset=Pokemons.offset+20
            Pokemons.show_list(self)
        if next == 'n':
            Pokemons.pokemon_names.clear ()
            Pokemons.offset = 0
