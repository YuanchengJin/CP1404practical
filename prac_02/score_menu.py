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
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = float(input("Enter score: "))
    return score
def print_result(score):
    # analyse the score and print the result
    if score < 50:
        print("Bad")
    elif score < 90:
        print("Passable")
    else:
        print('Excellent')
def show_stars(score):
    print("*" * int(score))

main()