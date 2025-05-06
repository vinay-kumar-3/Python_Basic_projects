print("🔤   Vowel Counter   🔤")

# vowels = ['a', 'e', 'i', 'o', 'u']

# while True:
#     count = 0
#     text = input("Enter some text (or 'quit'): ")
#     if text.lower() == 'quit':
#         break
#     for i in text:
#         if i in vowels:
#             count += 1

#     print(f"That text has {count} vowels!\n")

while True:
    text = input("\nEnter some text (or 'quit'): ")

    if text.lower() == 'quit':
        print("GoodBye")
        break

    count = sum([1 for char in text if char in "aeiou"])

    print(f"This text has {count} vowels!")
