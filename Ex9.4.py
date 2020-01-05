fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
countByEmail = dict()
for line in fh:
    if line.startswith("From:"):
        pieces = line.rstrip().split()
        email = pieces[1]
        countByEmail[email] = countByEmail.get(email, 0) + 1

maxEmailCount = None
emailWithMaxCount = None
for k,v in countByEmail.items():
    if maxEmailCount is None or v >= maxEmailCount:
        maxEmailCount = v
        emailWithMaxCount = k


print(emailWithMaxCount + " " + str(maxEmailCount))