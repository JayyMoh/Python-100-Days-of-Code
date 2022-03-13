# ===== Calculator Program =====

# ===== Imports =====
from Art import logo


def calculator():
    # ===== Welcome =====
    print("==============================================================================================================")
    print(logo)
    print("==============================================================================================================\n")

    # ===== Calculate functions =====
    def add(n1, n2):
        output = n1 + n2
        return output

    def subtract(n1, n2):
        output = n1 - n2
        return output

    def multiply(n1, n2):
        output = n1 * n2
        return output

    def divide(n1, n2):
        output = n1 / n2
        return output

    def calculate(n1,  n2):
        if operation == '+':
            answer = add(n1, n2)
        elif operation == '-':
            answer = subtract(n1, n2)
        elif operation == '*':
            answer = multiply(n1, n2)
        elif operation == '/':
            answer = divide(n1, n2)
        return answer             


    # ===== Operators =====
    operators = ['+', '-', '*', '/']

    # ===== Loop condition =====
    end_calculation = False
        
    # ===== Get first number =====
    first_number = int(raw_input("What's the first number?: "))

    # ===== Calculator loop =====
    while not end_calculation:
        # ===== Get the operator =====
        for operator in operators:
            print(operator)
            
        operation = raw_input("Pick an operation: ")

        # ===== Get the second number =====
        second_number = int(raw_input("What's the second number?: "))    
        
        # ===== Get the answer and store it =====                
        answer = str(calculate(first_number, second_number))
        print(answer)
        
        # ===== Check if user continues =====
        user_action = raw_input("Type 'y' to continue calculating with " + answer + ", or type 'n' to start a new calculation: ")
        
        if user_action == 'y':
            first_number = int(answer) 
        elif user_action == 'n':
            end_calculation = True
            calculator()
        

calculator()