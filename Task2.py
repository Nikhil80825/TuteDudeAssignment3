import math

n = float(input("Enter a number: "))

square_root = math.sqrt(n)
logarithm = math.log(n)
sin_value = math.sin(n)

if n <= 0:
    print("Enter a positive number or greater than zero.")
else:
    print(f"Square root :{square_root}")
    print(f"Logarithm :{logarithm}")
    print(f"Sine :{sin_value}")