import time
import datetime
print()
print("Welcome To Doug's Pizzeria - Online Ordering!")
print()
print("*** Pizza Menu ***")

prompt = "\nPlease enter your pizza topping:"
prompt += "\n(Enter 'done' when you are finished.) "
while True:
    topping = input(prompt)

    if topping == 'done':
        break
    else:
        print("Adding " + topping + ".")
print("\nFinished making your pizza - your wait time until delivery is 30 minutes!")
print("\nThanks for placing your order online with Doug's Pizzeria!")
print()
now_date = datetime.date.today()
now_now = time.strftime("%H:%M %p")
print(f"Date: {now_date}\nTime: {now_now}")
print()
