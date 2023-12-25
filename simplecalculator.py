def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
print("1-Addition")
print("2-Subtraction")
print("3-Multiplication")
print("4-Divide")
choice = int(input("Select the operation you want from the above table"))

if(choice == 1) :
  result = add(num1,num2)
  print(f"The addition of {num1} and {num2} is {result}")
elif(choice == 2) :
  result = subtract(num1,num2)
  print(f"The subtract of {num1} and {num2} is {result}")
elif(choice == 3) :
  result = multiply(num1,num2)
  print(f"The multiply of {num1} and {num2} is {result}")
elif(choice == 4) :
  result = divide(num1,num2)      

  print(f"The divide of {num1} and {num2} is {result}")
else :
  print("You enter a invalid number,Good Bye")
