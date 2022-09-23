def get_formatted_name(first, last):
    """generate a neatly formateed name"""
    full_name = f"{first} {last}"
    return full_name.title()

wife = get_formatted_name("iyayi", "ogbebor")
print(wife)

