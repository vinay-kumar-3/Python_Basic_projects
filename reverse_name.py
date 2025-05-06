print("REVERSE NAME GENERATOR\n")

while True:
    name = input("Enter a name: ")
    reversed_name = name[::-1]
    print(f"Your reversed name is: {reversed_name}")
    print(f"In a parallel universe, they call you {reversed_name.title()} !\n")

    again = input("Try another name? (y/n):\n")
    if again.lower() == 'n':
        break
