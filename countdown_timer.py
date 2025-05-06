import time

print("=== ⏰ COUNTDOWN TIMER ⏰ ===")
print("✨ count down from you chosen seconds! ✨")

while True:
    try:
        seconds = int(input("\n🤔 Enter seconts to countdown from : "))

        if seconds <= 0:
            print("❌ Please enter a positive number")
            continue

        print(f"⏳ Starting countdown from {seconds} seconds!")

        for i in range(seconds, 0, -1):
            print(f" {i} seconds remaining.....")
            time.sleep(1)

        print("\n🎉 CountDown Completed")

        again = input("\n🔄 Start another countdown ? (yes/no) : ").lower()

        if not again.startswith('y'):
            break
    except ValueError:
        print("❌ Please enter a number")
