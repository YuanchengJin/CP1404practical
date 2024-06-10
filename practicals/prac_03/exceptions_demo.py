"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur if the user inputs something that cannot be converted to an integer when prompted to enter the numerator or the denominator.
2. When will a ZeroDivisionError occur?
    A: Division by zero is undefined in mathematics and will raise a ZeroDivisionError in Python.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?

"""
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")"""
valid_input = False
while not valid_input:
    try:
       numerator = int(input("Enter the numerator: "))
       denominator = int(input("Enter the denominator: "))
       while denominator == 0:
            print("Cannot divide by zero!")
            denominator = int(input("Enter the denominator: "))
       fraction = numerator / denominator
       print(fraction)
       valid_input = False
    except ValueError:
        print("Must be valid number!")
print("Finished.")