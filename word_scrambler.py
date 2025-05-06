import random
print("🔄   WORD SCRAMBLER  🔄")

while True:
    word = input("enter a word to scramble (or 'quit'): ")
    if word.lower() == 'quit':
        print("🖐️   GoodBye")
        break
    letters = list(word)
    random.shuffle(letters)
    print("Scrambled:", "".join(letters))
