def add (a, b):
    return a + b
def subtract (a, b):
    return a - b
def multiplication (a, b):
    return a * b
def division (a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
def modulus (a, b):
    if b == 0:
        return "Error: modulus by zero is not allowed."
    return a % b

def calculator():
    print("select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")

    choice = input("Enter your choice number (1/2/3/4/5): ")
    if choice in ('1','2','3','4','5'):

        try:
            num_1 = float(input("Enter your first number: "))
            num_2 = float(input("Enter your second number: "))

            if choice =='1':
                result = add(num_1, num_2)
                print(f"{num_1} + {num_2} = {result}")
            elif choice == '2':
                result = subtract(num_1, num_2)
                print(f"{num_1} - {num_2} = {result}")
            elif choice == '3':
                result = multiplication(num_1, num_2)
                print(f"{num_1} * {num_2} = {result}")
            elif choice == '4':
                result = division(num_1, num_2)
                print(f"{num_1} / {num_2} = {result}")
            elif choice == '5':
                result = modulus(num_1, num_2)
                print(f"{num_1} % {num_2} = {result}")
        except ValueError:
            print("Error please enter your valid number")
    else:
        print("Invalid choice, select valid choice")

calculator()




