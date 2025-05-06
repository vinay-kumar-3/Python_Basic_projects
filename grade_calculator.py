print("📊   GRADE CALCULATOR    📊")

scores = []

while True:
    score = input("Enter a test score (or 'done'): ")
    if score.lower() == 'done':
        print("GoodBye  🖐️")
        break
    scores.append(float(score))
    avg_score = sum(scores) / len(scores)

    print(f"Average score is {avg_score:.1f}")
    if avg_score >= 90:
        print("Grade A")
    elif avg_score >= 80:
        print("Grade B")
    elif avg_score >= 70:
        print("Grade C")
    elif avg_score >= 60:
        print("Grade D")
    elif avg_score >= 50:
        print("Grade E")
    else:
        print("Grade F")
