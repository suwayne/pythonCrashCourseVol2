def describe_city(city, country='Iceland'):
    detail = (f"{city} is in {country}.")
    return detail.title()


detail = describe_city('los angeles')
print(detail)
print()
detail = describe_city('lagos', country='nigeria')
print(detail)
print()
detail = describe_city('sharja', 'united arab emirates')
print(detail)
