score = input("Enter Score: ")
try:
    fscore = float(score)
except:
    print("Please Enter a valid number")
    quit()
if fscore >= 0.9:
    grade = "A"
elif fscore >= 0.8:
    grade = "B"
elif fscore >= 0.7:
    grade = "C"
elif fscore >= 0.6:
    grade = "D"
elif fscore >= 0.8:
    grade = "B"
else:
    grade = "F"
print(grade)