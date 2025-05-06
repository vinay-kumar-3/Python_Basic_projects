print("🔄   TEXT FORMATTER  🔄")

text = input("enter some text : ")
print('1.UPPERCASE\n2.lowercase\n3.Title Case\n4.Sentence case')

choice = int(input("Choose a format (1-4): "))

if choice == 1:
    text = text.upper()
    print(text)
elif choice == 2:
    print(text.lower())
elif choice == 3:
    print(text.title())
else:
    print(text.capitalize())
