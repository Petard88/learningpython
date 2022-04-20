def city_country(city_name, country='sweden'):
    full = f"{city_name}, {country}"
    return full.title()

kumla = city_country('Kumla')
london = city_country('london', 'england')
japp = city_country('Örebro')
print(japp)
print(city_country('stockholm'))
print(kumla)
print(london)