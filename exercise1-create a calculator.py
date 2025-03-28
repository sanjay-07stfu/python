
print("\t\t****************************   BASIC CALCULATOR  ********************************")
print("1: ADDITION", "2: SUBTRACTION", "3: DIVISION", "4: MULTIPLICATION")

# Taking user input
choice = int(input("Enter your choice between 1 to 4: "))

# Check if the choice is valid before taking numbers
if choice in [1, 2, 3, 4]:  
    a = int(input("Enter the first number: "))  
    b = int(input("Enter the second number: "))  

    # Performing the operation based on the choice
    if choice == 1:
        result = a + b
    elif choice == 2:
        result = a - b
    elif choice == 3:
        # Handling division by zero error
        if b == 0:
            print("Error: Division by zero is not allowed.")
            exit()
        result = a / b
    elif choice == 4:
        result = a * b

    print(f"Result: {result}")

else:
    print("Invalid operation. Please enter a number between 1 and 4.")
