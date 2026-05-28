while True:
    print("----- CALCULATOR -----")
    
    print("1. Addition")
    print("2. Subtraction")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Choose an operation: "))

    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    if choice == 1:
         addition = number1 + number2
         print("Addition =", addition)
    elif choice == 2:
        subtraction = number1 - number2
        print("Subtraction =", subtraction)
    elif choice == 3:
        multiplication = number1 * number2
        print("Multiplication =", multiplication)
    elif choice == 4:
        if number2 == 0:
            print("Error")
        else :
            division = number1 / number2
            print ("Division =", division)
    else :
        print("Invalid Choice")

    print("Calculation Complete")

    again = input("Continue? ")
    if again == "no":
         break