"""display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>"""
MINI_SCORE = 0
MAX_SCORE = 100
PASS_THREEFOLD = 50
EXCELLENT_SCORE = 90
def main():
    score = 0
    display_menu()
    choice = input("Choose a letter please!").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        else:
            print("invalid input,please try again!")
        display_menu()
        choice = input("Choose from C, F, Q: ").upper()
    print("Good bye!")


def display_menu():
    # display the menu
    print("(G)et a valid score (must be 0-100 inclusive)")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")



def get_score():
    # get score from user.
    score = float(input("Enter score: "))
    while score < MINI_SCORE or score > MAX_SCORE:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = float(input("Enter score: "))
    return score
def print_result(score):
    # analyse the score and print the result
    if score < PASS_THREEFOLD:
        print("Bad")
    elif score < EXCELLENT_SCORE:
        print("Passable")
    else:
        print('Excellent')
def show_stars(score):
    print("*" * int(score))

main()