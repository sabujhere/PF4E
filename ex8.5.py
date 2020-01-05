fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = list()
for line in fh:
    if line.startswith("From:"):
        pieces = line.rstrip().split()
        email = pieces[1]
        print(email)
        lst.append(email)
        count = count + 1
print("There were", count, "lines in the file with From as the first word")