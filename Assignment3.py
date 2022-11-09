score = float(input("Enter Score between 0.0 and 1.0: "))

try:
    if 1.0 >= score >= 0.9:
        print("A")
    elif 0.89 >= score >= 0.8:
        print("B")
    elif 0.79 >= score >= 0.7:
        print("C")
    elif 0.69>= score >= 0.6:
        print("D")
    elif 0 < score < 0.6:
        print("F")
        
except:
    print("Value out of range.")
    