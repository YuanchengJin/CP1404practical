"""   Number: 5
   Number: 20
   Number: 1
   Number: 2
   Number: 3
   The first number is 5
   The last number is 3
   The smallest number is 1
   The largest number is 20
   The average of the numbers is 6.2"""
def main():
    # Main function to get numbers, print them, and display statistical results.
    numbers = get_numbers_from_user()
    print_numbers(numbers)
    display_results(numbers)

def get_numbers_from_user():
    # Prompt the user to input a series of numbers and return them as a list.
    numbers = []
    for i in range(5):
        number = int(input("Please enter 5 numbers: "))
        numbers.append(number)
    return numbers
def print_numbers(numbers):
    # Print 5 numbers
    for number in numbers:
        print(f"Number: {number}")
def display_results(numbers):
    # Display the first, last, smallest, largest, and average of the numbers.
    first_number = numbers[0]
    last_number = numbers[-1]
    smallest_number = min(numbers)
    largest_number = max(numbers)
    average_number = sum(numbers) / len(numbers)
    print(f"The first number is {first_number}")
    print(f"The last number is {last_number}")
    print(f"The smallest number is {smallest_number}")
    print(f"The largest number is {largest_number}")
    print(f"The average of the numbers is {average_number:.1f}")

main()


