import re

fname = input("Enter file name: ")
if len(fname) < 1: fname = "regex_sum_345106.txt"

fh = open(fname)
total = 0
for line in fh:
    numbers = re.findall("[0-9]+", line)
    for number in numbers:
        total = total + int(number)

print(total)
