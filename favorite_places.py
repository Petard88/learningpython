favorite_places = {
    'petter': ['köket', 'trädgården', 'källaren'],
    'sandra': ['altanen', 'trädgården', 'sängen'],
    'olle': ['förskolan', 'lekparken', 'soffan']
    }
for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")