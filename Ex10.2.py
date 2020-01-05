fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"

fh = open(fname)
count = 0
emailCountbyHour = dict()
for line in fh:
    if line.startswith("From"):
        pieces = line.rstrip().split()
        if len(pieces) < 5:
            continue
        hour = pieces[5].split(':')[0]
        emailCountbyHour[hour] = emailCountbyHour.get(hour, 0) + 1

for k,v in sorted(emailCountbyHour.items()):
    print(k,v)
