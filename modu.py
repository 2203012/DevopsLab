# Modulus of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if b != 0:
    mod_result = a % b
    print("Remainder:", mod_result)
else:
    print("Error: Cannot perform modulus with zero!")
