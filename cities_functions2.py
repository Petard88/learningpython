def describe_city(city_name, country_name='Sweden'):
    print(f"{city_name.title()} is a city in {country_name.title()}.")


describe_city('örebro')
describe_city('stockholm')
describe_city('london', 'england')