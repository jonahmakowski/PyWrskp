# Import the math module to access mathematical functions
import math

def main():
  # Print a welcome message
  print("Welcome to the scientific calculator!")
  
  # Prompt the user for the first number
  num1 = float(input("Enter the first number: "))
  
  # Prompt the user for the second number
  num2 = float(input("Enter the second number: "))
  
  # Prompt the user for the operation
  op = input("Enter the operation (+, -, *, /, ^): ")
  
  # Calculate the result
  result = 0
  if op == "+":
    result = num1 + num2
  elif op == "-":
    result = num1 - num2
  elif op == "*":
    result = num1 * num2
  elif op == "/":
    result = num1 / num2
  elif op == "^":
    result = num1 ** num2
  else:
    print("Invalid operator")
  
  # Print the result
  print("Result: ", result)

# Call the main function
if __name__ == "__main__":
  main()
  