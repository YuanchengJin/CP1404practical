def main():
    """Display menu for temperature conversion"""
    display_menu()
    choice = input("Choose from C, F, Q: ").upper()
    while choice != 'Q':
        if choice == 'C':
            celsius = float(input("Enter Celsius:  "))
            fahrenheit = transfer_celsius_to_fahrenheit(celsius)
            print(f"Converted fahrenheit is : {fahrenheit:.2f} F")
        elif choice == 'F':
            fahrenheit = float(input("Enter fahrenheit:  "))
            celsius = transfer_fahrenheit_to_celsius(fahrenheit)
            print(f"Converted fahrenheit is : {celsius:.2f} F")
        else:
            print("Invalid input,try again! ")
        display_menu()
        choice = input("Choose from C, F, Q: ").upper()

def display_menu():
    # Display the menu
    print("C - Convert Celsius to Fahrenheit")
    print("F - Convert Fahrenheit to Celsius")
    print("Q - Quit")
def transfer_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit and return the result."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def transfer_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius and return the result."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

main()