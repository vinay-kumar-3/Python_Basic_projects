import random
print("=== 🎮  COIN FLIP GAME 🎮 ===")

print("✨ Guess heads or tails! ✨")

while True:
    guess = input("\n🤔 Enter your Guess (heads/tails): ")

    if guess != 'heads' or guess != 'tails':
        print("❌ Please enter 'heads' or 'tails' ❌")
        continue

    flip = random.choice(["heads", "tails"])
    print(f"\n🪙 The coin shows: {flip} 🪙")

    if guess.lower() == flip:
        print("🎉 You guessed correctly ! You win! 🏆")
    else:
        print("😢 Sorry, wrong guess. Try again")

    again = input("\n🔄 Play again? (yes/no) : ")
    if again.lower() == 'no':
        print("🖐️   Thank you for playing !")
        break
