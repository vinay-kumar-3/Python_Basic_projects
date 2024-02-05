# The Caesar cipher shifts all the letters in a piece of text by a certain number of places. The key for this cipher is a letter which represents the number of place for the shift

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def conversion(direction,text,shift):
    cipher_text =""
    for i in text:
        if direction == 'encode':
            n = alphabet.index(i) + shift
        else:
            n = alphabet.index(i) - shift
        if n > 25:
            n -=26
        cipher_text+=alphabet[n]
    print("converted Text : ",cipher_text)

n= True
while n:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    conversion(direction,text,shift)

    k = input("if your continue then type YES otherwise NO:\n").lower()
    if k == 'no':
        n = False
