cities = {
    'örebro': {
        'country': 'sweden',
        'population': '>1',
        'fact': 'has a svamp',
    },
    'stockholm': {
        'country': 'sweden',
        'population': '>5',
        'fact': 'has a vasaskepp',
    },
    'london': {
        'country': 'england',
        'population': '>10',
        'fact': 'has a big ben',
    },
}

print(cities)

for city, info in cities.items():
    print(f"\nCity: {city.title()}.")
    country = info['country']
    population = info['population']
    fact = info['fact']
    print(f"\tlocated in {country.title()}\n\thas a population of {population.title()}\n\trandom fact: {fact}")