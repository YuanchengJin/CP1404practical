"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

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
    if score < 0 or score > 100:
        print("Invalid score")
    elif score < 50:
        print("Bad")
    elif score < 90:
        print("Passable")
    else:
        print('Excellent')
main()