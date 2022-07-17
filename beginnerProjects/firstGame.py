print("welcome to my first game!")
name = input("what is your name? ")
age = int(input("what is your age? "))

print("hello", name, "you are", age, "years old.")

if age >= 18:
    print("you are old enough to play")
    wants_to_play = input("do you want to play?").lower()
    if wants_to_play == "yes":
        print("lets play!")

        left_or_right = input("first choice... left or right?(left/right)? ")
        if left_or_right == "left":
            ans = input("nice!, you followed the pay and reached a lake... Do you swim across or go around (across/around)? ")

            if ans == "around":
                print("you went around and reached the other side of the lake")
            elif ans == "across":
                print("you managed to get across, but were bit by a fish and lost 5 health.")
            else:
                print("you lost.")

        else:
            print("you fell down and lost")

    else:
        print("cya...")    

else:
    print("you are not old enough to play...")




