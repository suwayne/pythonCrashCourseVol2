def city_country(city, country):
    country_detail = (f"{city}, {country}.")
    return country_detail.title()


country_detail = city_country('yokohama', 'japan')
country_detail = city_country('lagos', 'nigeria')
country_detail = city_country('rio', 'brazil')
country_detail = city_country('abu dhabi', 'uae')
print(country_detail)
