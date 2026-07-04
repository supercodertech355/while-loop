# Get the base and exponent from the user
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent (integer): "))

# Initialize result and loop counter
result = 1.0
count = abs(exponent)

# Multiply the base by itself 'exponent' times
while count > 0:
    result *= base
    count -= 1

# Handle negative exponents (e.g., 2^-3 = 1 / (2^3))
if exponent < 0:
    result = 1.0 / result

# Display the final answer
print(f"{base} raised to the power of {exponent} is: {result}")
