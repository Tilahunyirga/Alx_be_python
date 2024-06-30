num1 = int(input("enter the first number:"));
num2 = int(input("enter the second number:"));
operation =(input("choose the operation (+, -, *, /):"));

match operation:
    case "+":
        print(int(num1+num2))
    case "-":
        print(f'the result is {num1-num2}.')
    case "*":
        print(f'the result is {num1*num2}.')
    case "/":
        if num2 ==0:
            print(f"can't divide by zero.")
        else:
            print(f'the result is {num1/num2}.')