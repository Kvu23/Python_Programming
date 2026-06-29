#program to understand the match case statement in python
Day = int(input("Enter the day of the week (1-7): "))
print("You entered: ", Day)


match Day:
    case 1:
        print("The Day of the week is Monday")
    case 2:
        print("The Day of the week is Tuesday")
    case 3:
        print("The Day of the week is Wednesday")
    case 4:
        print("The Day of the week is Thursday")
    case 5:
        print("The Day of the week is Friday")
    case 6:
        print("The Day of the week is Saturday")
    case 7:
        print("The Day of the week is Sunday")
    case _:
        print("Invalid day of the week")
