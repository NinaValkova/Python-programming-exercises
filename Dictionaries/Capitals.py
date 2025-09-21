countries_line = input()
capitals_line = input()

countries = countries_line.split(', ')
capitals = capitals_line.split(', ')

country_capital = {}
size = len(countries)
for i in range(0, size, 1):
    country_capital[countries[i]] = capitals[i]

for country, capital in country_capital.items():
    print(f'{country} -> {capital}')
    