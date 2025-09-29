def perform_operation(num1, num2, operation):
    operations = ("add", "subtract", "multiply", "divide")

    if operation in operations:
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 != 0:
                return num1 / num2
            else:
                print ("Error cannot divide by zero!")
    else:
        print ("The operation provided is Invalid!")

