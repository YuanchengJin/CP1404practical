import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def main():
    # Generate and print quick picks based on user input.
    num_of_picks = int(input("How many quick picks? "))
    for i in range(num_of_picks):
        quick_pick = get_random_numbers()
        print(" ".join(f"{number:2}" for number in quick_pick))
def get_random_numbers():
    # Generate and return a sorted list of NUMBERS_PER_PICK unique random numbers.
    picks = []
    while len(picks) < NUMBERS_PER_PICK:
        pick = random.randint(MIN_NUMBER, MAX_NUMBER)
        if pick not in picks:
            picks.append(pick)
    picks.sort()
    return picks

main()