print("🚶 STEP COUNTER 🚶\n")

daily_goal = int(input("🥅  What is daily step goal? "))
today_steps = int(input("✨ How many steps have you taken today? "))

remaining = daily_goal - today_steps

if remaining == 0:
    print("🎉   Congrats! You Successfully reached your goal")
elif remaining < 0:
    print(f"🥳  Congratulations! You've exceeded your goal by { -remaining } steps")
elif remaining > 0:
    print(f"💪  You need {remaining} more steps to reach goal")
