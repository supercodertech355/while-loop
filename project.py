# Get input from the user
number = int(input("Enter an integer: "))

# Initialize the reversed number variable
reversed_number = 0

# Store the original number for the final output
original_number = number

# Handle negative numbers by working with the absolute value
temp_number = abs(number)

# Loop to reverse the digits
while temp_number > 0:
    # Get the last digit
    digit = temp_number % 10
    
    # Append the digit to the reversed number
    reversed_number = (reversed_number * 10) + digit
    
    # Remove the last digit from the temporary number
    temp_number = temp_number // 10

# Restore the negative sign if the original number was negative
if original_number < 0:
    reversed_number = -reversed_number

# Display the result
print(f"The reversed number is: {reversed_number}")
