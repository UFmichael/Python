#A simple python program to work as a calculator
#Last modified 7/19/2022

valid1 = True
valid2 = True
valid3 = False #to add variation and demonstrate that negative coding also works

def calculator(x, y, operation):
  
  #return a answer after solving the mathematical expression using inputs

  if operation == "+":
    return x + y 
  elif operation == "-":
    return x - y 
  elif operation == "*":
    return x * y 
  else: # operation == "/"
    return x / y 

def result(operation):

  #return the result type
  
  if operation == "+":
    result_type = "sum"
  elif operation == "-":
    result_type = "difference" 
  elif operation == "*":
    result_type = "product"
  else: 
    result_type = "quotient"
  
  return result_type


#to ensure the values input are numbers
while valid1:
  try:
    a = float(input("Enter your first number : "))
    
    valid1 = False
  except ValueError:
    print("That's not a number. Please input a number.")

while valid2:
  try:
    b = float(input("Enter your second number : "))
    
    valid2 = False
  except ValueError:
    print("That's not a number. Please input a number.")

#Inquire about the user's desired operation
print("What operation would you like to do?")
# to ensure o is a valid operation
while not valid3:
  
  o = input("Operation: ")

  if o == "+":
    valid3 = True
  elif o == "-":
    valid3 = True
  elif o == "*":
    valid3 = True
  elif o == "/":
    valid3 = True
  else:
    print("That was not a valid operation. Valid operations are +, -, *, or /")

# a = input("Enter your first number: ")
# b = input("Enter your second number: ")
# o = input("What operation would you like to do? (Only +, -, *, or /) \nOperation :")

ans = calculator(a,b,o)
rsult = result(o)

print("Your requested calculation: " + str(a) + " " + o + " " + str(b))
print("The " + rsult + " is " + str(ans))