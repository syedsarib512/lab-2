def calculator():
    print("Welcome to My Calculator")
    print("Instructions \nType A for Addition \nType S for Substraction \nType M for Multiplication \nType D for Division \nType R for Modulus \nType E for Exit")
    cmd = input("Enter your Choice here : ")
    if cmd == 'E':
        return 
    nmbr1 = int(input("Enter first digit : "))
    nmbr2 = int(input("Enter second digit : "))
    if cmd == "A":
        print(f'Output is {nmbr1 + nmbr2}')
        print(calculator())
    elif cmd == 'S':
        print(f'Output is {nmbr1 - nmbr2}')
        print(calculator())
    elif cmd == 'M':
        print(f'Output is {nmbr1 * nmbr2}')
        print(calculator())
    elif cmd == 'D':
        print(f'Output is {nmbr1 / nmbr2}')
        print(calculator())
    elif cmd == 'R':
        print(f'Output is {nmbr1 % nmbr2}')
        print(calculator())
    else:
        print('Invalid Command! Try Again!')
        print(calculator())
print(calculator())