try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle legth: "))
    
    if width == length:
        exit("That looks like a square.")
    
    area = width * length
    print(area)
except ValueError:
    print("Please enter a number.")