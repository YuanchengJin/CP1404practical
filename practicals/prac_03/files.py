"""1.Write code that asks the user for their name, then opens a file called name.txt and writes that name to it.
 Use open and close for this question."""
name = input("Enter your name,please!: ")
FILENAME = "name.txt"
out_file = open(FILENAME,'w')
print(name, file = out_file)
out_file.close()
"""2.In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as above)
 then prints (note the exact output),"""

FILENAME = "name.txt"
in_file = open(FILENAME)
text = in_file.read()
print("Your name is" + " " + text)
in_file.close()

"""3.Create a text file called numbers.txt and save it in your prac directory. 
Put the following three numbers on separate lines in the file and save it:"""
total = 0
FILENAME = "numbers.txt"
in_file = open(FILENAME)
for i in range(0,2):
    number = in_file.readline()
    total = total + int(number)
print(total)
in_file.close()

"""4.Now write a fourth block of code that prints the total for all lines in numbers.txt. This should work for a file with any number of numbers.
 Use with instead of open and close for this question."""
total = 0

with open('numbers.txt', 'r') as in_file:
    for line in in_file:
        total += int(line.strip())

print(f"Total sum: {total}")
