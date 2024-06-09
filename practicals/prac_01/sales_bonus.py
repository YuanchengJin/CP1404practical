"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
psudocode:
get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing"""
LOW_SALES_THRESHOLD = 1000
LOW_SALES_BONUS = 0.1
HIGH_SALES_BONUS = 0.15

sales = float(input("Enter sales:$"))
while sales >= 0:
    if sales <= LOW_SALES_THRESHOLD:
        bonus = LOW_SALES_BONUS * sales
    else:
        bonus = HIGH_SALES_BONUS * sales
    print(f'The bonus is $ {bonus:.2f}')
    sales = float(input("Enter sales:$"))
          