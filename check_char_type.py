print("📝 CHARACTER TYPE CHECKER 📝\n")

character = input("enter a single character: ")

# isalnum() is accepts both alpha characters and numeric
if character.isalpha():
    print("This is a letter.")
elif character.isdigit():
    print("This is a digit.")
else:
    print("This is a special character.")


'''
Note :
isalnum() --> Returns True if all characters are alphanumeric (letters or digits).
isalpha() --> Returns True if all characters are alphabetic (only letters).
isdigit() --> Returns True if all characters are digits.
isdecimal() --> Returns True if all characters are decimal characters (0–9).
isnumeric() --> Returns True if all characters are numeric (includes superscripts, etc.)
islower() --> Returns True if all characters are lowercase letters.
isupper() --> Returns True if all characters are uppercase letters.
isspace() --> Returns True if all characters are whitespace.
istitle() --> Returns True if the string is titlecased (e.g., "Hello World").
isprintable() --> Returns True if all characters are printable.
isascii() --> Returns True if all characters are ASCII (0–127).

'''
