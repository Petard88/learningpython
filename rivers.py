rivers_list = {'nile': 'egypt',
          'amazon': 'brazil',
          'yangtze': 'china',
          }

for river, country in rivers_list.items():
    print(f"The {river.title()} runs through {country.title()}")

for river in rivers_list.keys():
    print(f"The {river.title()}")

for country in rivers_list.values():
    print(f"{country.title()}")