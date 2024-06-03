def city_country(city_name, country_name, population=0):
    description = f'{city_name.title()}, {country_name.title()}'
    if population:
        description += f' - population {population}'
    return description