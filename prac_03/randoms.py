import random

print(random.randint(5, 20))  # line 1
# What did you see on line 1? 8
# What was the smallest number you could have seen, what was the largest? smallest：5 , largest:19
print(random.randrange(3, 10, 2))  # line 2
# What did you see on line 2?7
# What was the smallest number you could have seen, what was the largest? smallest:3  ,  smallest:9
# Could line 2 have produced a 4? No,it can only produce odds.
print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 3? 3.6820826588073787
# What was the smallest number you could have seen, what was the largest? 2.5

number = random.randint(0,100)
print(number)
