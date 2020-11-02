nested_list = [[0, 1, 2], [0, 1, 3], [0, 1, 4]]

replacement = {
    0: str('years'),
}

nested_list = [replacement.get(x, x) for x in nested_list[1]]
print(nested_list)
