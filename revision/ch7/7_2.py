#restaurant sitting:

groupSize = input("Hello customer, how many people are in your dinner group?: ")
if int(groupSize) > 8:
    print(f"Hello customer, sadly, you'll have to wait for anothe table. a group of {groupSize}")
    print(f"is larger than 8")
else:
    print("Hi customer, your table is ready")
