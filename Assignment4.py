hrs = input("Enter Hours:")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)

def computepay(h, r):
    if h > 40:
        return ((h - 40) * r * 1.5) + (40 * r)
    else:
        return (h * r)
    
p = computepay(h, r)
print("Pay", p)
