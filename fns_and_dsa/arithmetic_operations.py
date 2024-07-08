
def perform_operation(num1, num2, operation):
    match operation:
        case "add": return num1+num2
        case "subtract": return num1-num2
        case "multiply": return num1*num2
        case "divide":
            if num2 == 0:
                print("can not divide by zero")
            else: return num1/num2
        case _:
            return "incorrect input"

'''
def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1+num2
    elif operation ==  "subtract":
        return num1-num2
    elif operation == "multiply":
        return num1*num2
    elif operation == "divide":
        if num2 == 0 or num1 == 0:
            print("can not divide by zero")
        else:
            return num1/num2
    else:
        print("incorrect input")
'''