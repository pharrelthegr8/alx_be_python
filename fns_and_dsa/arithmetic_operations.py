def perform_operation(num1, num2, operation):
    operations = ("add", "subtract", "multiply", "divide")

    if operation in operations:
        match operation:
            case "add":
                return num1 + num2
            case "subtract":
                return num1 - num2
            case "multiply":
                return num1 * num2
            case "divide":
                if num2 != 0:
                    return num1 / num2
                else:
                    print ("Error cannot divide by zero!")
    else:
        print ("The operation provided is Invalid!")

