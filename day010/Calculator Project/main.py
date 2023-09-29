from art import logo

print(logo)

def add(n1, n2):
  """Takes two number inputs and returns the sum of the two values."""
  return n1 + n2
 
def subtract(n1, n2):
  """Takes two number inputs and returns the difference of the two values."""
  return n1 - n2
 
def multiply(n1, n2):
  """Takes two number inputs and returns the product of the two values."""
  return n1 * n2
 
def divide(n1, n2):
  """Takes two number inputs and returns the quotent of the two values."""
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  n1 = int(input("What the first number?: "))
  should_continue = True

  while should_continue:
    operation_select = input("Pick an operation: [+] [-] [*] [/] \n")
    n2 = int(input("What the second number?: "))
    calc_function = operations[operation_select]
    solution = calc_function(n1, n2)
    print(f"{n1} {operation_select} {n2} = {solution}")
  
    if input(f"Type 'y' to continue calculating with {solution}, or 'n' to start a new calculation \n") == 'y':
      n1 = solution
    else:
      should_continue = False
      calculator()


calculator()
