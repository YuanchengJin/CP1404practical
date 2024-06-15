"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    # Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)
    print("\nIncome Report\n-------------")
    print_report(months,incomes)

def print_report(months,incomes):
    # Print months and related incomes
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        # print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
        print(f"Month{month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()