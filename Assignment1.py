hrs = input("Enter Hours:")
rate = float(input("Enter rate: "))
h = float(hrs)
overtime = 0
if h > 40:
    overtime = h - 40
else:
    overtime = 0

total = (overtime * rate * 1.5) + ((h - overtime) * rate)
print(total)
