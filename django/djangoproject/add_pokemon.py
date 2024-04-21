from sys import argv, stdin

from csv import reader

from PIL import Image

import django
from django.db import transaction
from django.db.models import Q
from django.utils import timezone
from json import loads

django.setup()

from pokedex.models import Ability, EleType, Pokemon, PokemonImage, User


# Read stdin for paths to images
def add_images():
    pokemon_images = []
    
    for line in stdin:
        filename = line.strip()
        file_parts = filename.split("/")
        basename = file_parts[-1]

        #ext is ALWAYS '.png', but split by '.' just in case
        basename_parts = basename.split(".")[0].split("-")
        pokemon_number = basename_parts[0]

        # number 0 and non-numeric pokenumbers don't count. Skip em!
        if pokemon_number == "0" or not pokemon_number.isnumeric():
            continue

        important_parts = list()
        for part in file_parts[:-1] + basename_parts[1:]:
            if part in ["pokemon", "main-sprites", "black-white"]:
                pass
            else:
                important_parts.append(part)
        description=" ".join(important_parts).title()

        pokemon = Pokemon.objects.get(number=pokemon_number)

        dj_img = PokemonImage(
            pokemon=pokemon,
            description=description,
        )

        # Use Pillow to crop the image's blank space
        im = Image.open(filename)
        im2 = im.crop(im.getbbox())
        im2.save(filename)

        dj_img.image.save(basename, open(filename, 'br'))
        dj_img.save()

        if len(important_parts) == 0 or not pokemon.primary_image:
            pokemon.primary_image = dj_img
            pokemon.save()

    
    with transaction.atomic():
        PokemonImage.objects.bulk_create(pokemon_images)


# Read stdin for pokemon data 
def add_pokemon():
    ability_map = { x.name: x for x in Ability.objects.all() }

    for (abilities,against_bug,against_dark,against_dragon,
         against_electric,against_fairy,against_fight,against_fire,
         against_flying,against_ghost,against_grass,against_ground,
         against_ice,against_normal,against_poison,against_psychic,
         against_rock,against_steel,against_water,attack,
         base_egg_steps,base_happiness,base_total,capture_rate,
         classification,defense,experience_growth,height_m,hp,
         japanese_name,name,percentage_male,pokedex_number,sp_attack,
         sp_defense,speed,type1,type2,weight_kg,generation,is_legendary
    ) in reader(stdin):
        pokemon = Pokemon.objects.create(
                number=int(pokedex_number),
                name=name,
                classification=classification,
                height=float(height_m or "0"),
                weight=float(weight_kg or "0"),
                prevevolution=None,
            )

        # Adding many-to-many has to be done after the initial creation of the pokemon
        pokemon.type.add(*EleType.objects.filter(Q(name=type1) | Q(name=type2)))

        for ability_name in loads(abilities.replace("'", "\"").replace(";", ",")):
            pokemon.abilities.add(ability_map[ability_name])
        
        pokemon.save()

def add_poketypes():
    types = dict()

    # We need a reference to every EleType in order to set up the relationships, so
    # make a list of each relationship by *name*. and make it after
    add_no_effect = []
    add_strength = []
    add_weakness = []

    for typename,no_effect,strengths,weaknesses in reader(stdin):
        types[typename] = EleType(
            name=typename
        )
        add_no_effect.extend((typename, x) for x in no_effect.split())
        add_strength.extend((typename, x) for x in strengths.split())
        add_weakness.extend((typename, x) for x in weaknesses.split())

    with transaction.atomic():
        EleType.objects.bulk_create(types.values())

    # ...as two transactions
    with transaction.atomic():
        
        for x, y in add_no_effect:
            types[x].no_effect_on.add(types[y])

        for x, y in add_strength:
            types[x].effective.add(types[y])

        for x, y in add_weakness:
            types[x].weakness.add(types[y])

        for type in types.values():
            type.save()
            
def add_pokeabilities():
    with transaction.atomic():
        Ability.objects.bulk_create([
            Ability(abilityID=i, name=name, affect=desc)
            for i,(name,desc) in enumerate(reader(stdin))
        ])

def add_pokelutions():
    with transaction.atomic():
        for pokemon_number,number_evolved_from in reader(stdin):
            if not number_evolved_from:
                continue

            mon = Pokemon.objects.get(number=pokemon_number)
            pre_mon = Pokemon.objects.get(number=number_evolved_from)

            mon.prevevolution = pre_mon
            mon.save()


def check_pokemon_added():
    # there should be exactly 801 pokemon in the DB.
    if Pokemon.objects.count() == 801:
        exit(0)
    else:
        exit(2)

if __name__ == "__main__":
    cmd = argv[1]

    match cmd:
        case "pokemon_are_added":
            check_pokemon_added()
        case "images":
            add_images()
        case "pokemon":
            add_pokemon()
        case "poketypes":
            add_poketypes()
        case "pokeabilities":
            add_pokeabilities()
        case "pokelutions":
            add_pokelutions()
    