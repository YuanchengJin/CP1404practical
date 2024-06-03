"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
MINI_SCORE = 0
MAX_SCORE = 100
PASS_THREEFOLD = 50
EXCELLENT_SCORE = 90
def main():
    # ask the user for their score and print the result.
    score = get_score()
    print_score(score)
def get_score():
    # get score from user.
    score = float(input("Enter score: "))
    return score
def print_score(score):
    # analyse the score and print the result
    if score < MINI_SCORE or score > MAX_SCORE:
        print("Invalid score")
    elif score < PASS_THREEFOLD:
        print("Bad")
    elif score < EXCELLENT_SCORE:
        print("Passable")
    else:
        print('Excellent')
main()