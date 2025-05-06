def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by Zero is not allowed"
    return x/y


def main():
    print("\n=== SIMPLE CALCULATOR ===")
    print("Select operation:")
    print("1. ➕  Addition")
    print("2. ➖  Subtraction")
    print("3. ✖️   Multiplication")
    print("4. ➗  Division")

    while True:
        try:
            choice = int(input("\nEnter Choice (1-4) : "))

            if choice not in [1, 2, 3, 4]:
                print("Please chosen between 1 to 4")
                continue

            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            if choice == 1:
                print(f"\n{x} + {y} = {add(x,y)}")
            elif choice == 2:
                print(f"\n{x} - {y} = {subtract(x,y)}")
            elif choice == 3:
                print(f"\n{x} * {y} = {multiply(x,y)}")
            else:
                print(f"\n{x} / {y} = {divide(x,y)}")

            again = input(
                "\nDo you want perform another calculation? (yes/no): ").lower()

            if not again.startswith('y'):
                print("Thank you for Using Calculator")
                break
        except ValueError:
            print("Please enter a number")


if __name__ == "__main__":
    main()
