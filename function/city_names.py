def city_country(city, country):
    formatted = f'{city.title()}, {country.title()}'
    print(formatted)
    return formatted

city_country('paris', 'france')
city_country('porto', 'portugal')
city_country('brisbane', 'australia')