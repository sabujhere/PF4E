fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for piece in line.rstrip().split():
        if lst.count(piece) == 0:
            lst.append(piece)
lst.sort()
print(lst)
