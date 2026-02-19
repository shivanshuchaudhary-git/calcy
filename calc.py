import art
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b



operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}


def calculator():
    print(art.logo)
    should_continue = True
    a1 = float(input("Enter first number: "))
    while should_continue:


        for symbol in operations:
            print(symbol)
        operation_symbol = input("Enter operation: ")
        a2 = float(input("Enter second number: "))
        answer = operations[operation_symbol](a1, a2)
        print(f"{a1} {operation_symbol} {a2} = {answer} ")

        choice = input(f"Do you want to continue with {answer} ? type' y 'for yes and 'n' for no: ")

        if choice == 'y':
            a1 = answer
        else:
           should_continue = False
           print("\n" * 20)
           calculator()


calculator()