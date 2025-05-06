import random
import time

# word pairs => (prompt: related words)
word_pairs = {
    "sky": ["blue", "cloud", "bird", "fly", "sun"],
    "water": ["drink", "ocean", "swim", "fish", "boat"],
    "food": ["eat", "cook", "tasty", "meal", "restaurant"],
    "music": ["song", "dance", "listen", "band", "rhythm"],
    "book": ["read", "story", "page", "author", "library"],
    "tree": ["leaf", "green", "forest", "wood", "shade"],
    "car": ["drive", "road", "wheel", "travel", "speed"],
    "dog": ["pet", "bark", "walk", "loyal", "puppy"]
}

score = 0
rounds = 0

print("\n=== 🔄 WORD ASSOCIATION GAME 🔄 ===")
print("✨ Respond with a related word quickly! ✨")

while True:
    prompt = random.choice(list(word_pairs.keys()))

    print(f"\n🔤 Prompt word: {prompt.upper()}")
    print("Quick! Type a word related to this prompt!")

    start_time = time.time()

    response = input(">>> ").lower().strip()
    response_time = time.time() - start_time

    print("response time", response_time)

    if response in word_pairs[prompt]:
        points = max(1, 5 - int(response_time))
        score += points
        print(
            f"✅ Good association! +{points} points (answered in {response_time:.1f}s)")
    else:
        print(
            f"❌ Not a common association. Related words included: {', '.join(word_pairs[prompt])}")

    rounds += 1
    print(f"Score: {score}/{rounds * 5} possible points")

    # Ask to play again
    if input("\n🔄 Play again? (yes/no): ").lower().startswith('n'):
        print(f"Final score: {score}. Thanks for playing! 👋")
        break
