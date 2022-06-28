#amusement park.py

age = 12

if age < 4:
    print("your admission cost is $0.")
elif age < 18:
    print("your admission cost is $25.")
else:
    print("your admission cost is $40.")


#any age greater that 17 will cause the first 2 tests to fail.

age = 20

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"your admission cost is ${price}")

