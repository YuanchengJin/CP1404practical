"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
MINI_SCORE = 0
MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASS_THRESHOLD = 50

score = float(input("Enter score: "))
if score < MINI_SCORE or score > MAX_SCORE:
    print("Invalid score")
elif score < PASS_THRESHOLD:
    print("Bad")
elif score < EXCELLENT_SCORE:
    print("Passable")
else:
    print('Excellent')