from art import logo
print(logo)

def add(a,b):
  return a+b
def substract(a,b):
  return a-b
def divide(a,b):
  return a/b
def multiply(a,b):
  return a*b

operations={
  "+":add,
  "-":substract,
  "*":multiply,
  "/":divide,
}

"""Adding Recursive to the program"""
def calculator():
  num1=float(input("What's the first number? " ))
  for symbol in operations:
    print(symbol)
  """Setting flag"""
  should_continue=True

  """Loop to control our program to run many times"""
  while should_continue:
    operation_symbol=input("Pick an operation  ")
    num2=float(input("What's the next number? " ))
    calculation_function=operations[operation_symbol]
    answer=calculation_function(num1,num2)
  
    print(f"{num1} {operation_symbol} {num2}={answer}")
    if input(f"Type 'y' to continue or with {answer} or 'n' to start new calculation")=='y':
      num1=answer
    else:
      should_continue=False
      calculator()
calculator()
                 

