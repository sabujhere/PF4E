def computepay(h, r):
    overtime = hrs - 40
    overtime_pay = 0
    if overtime > 0:
        overtime_pay = overtime * rate * 1.5
    return abs(hrs - overtime) * rate + overtime_pay


hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

print(computepay(hrs, rate))
