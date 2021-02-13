
print("Welcome to Odd or Even, hit q to quit.")

num = None

while num != "q":

    num = input("What number are you thinking? ")

    try:

        num = int(num)

        if num % 2 == 0:
            print(f"{num} is even")

        elif num % 2 != 0:
            print(f"{num} is odd")

    except:

        if num != 'q':
            print('Invalid input, try again')
        else:
            print("Thanks for playing!")
