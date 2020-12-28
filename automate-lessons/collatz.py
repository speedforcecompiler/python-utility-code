choice = 1
while choice == 1:
    try:
        # global choice
        number = int(input("Enter a number : "))
        while number > 1:
            if number%2 == 0:
                number = number/2
            else:
                number = (3*number + 1)/2
            print(number)
        # print("Do you wish to enter another number?\n0 : No\n1 : Yes")
        choice = int(input("Do you wish to enter another number?\n0 : No\n1 : Yes\nEnter Choice : "))
    except ValueError:
        print("Please enter a valid number!")