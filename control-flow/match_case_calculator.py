num1 = int(input("Enter the First number:"))
num2 = int(input  ("Enter the second number: "))
operations = input ("Choose the operation (+, -, *, /):")

match operations:
    case "+":
        print("The result is", num1 + num2)
    case "-":
        print("The result is", num1 - num2)   
    case "*":
        print("The result is", num1 * num2)
    case "/":
        if num2 == 0:
             print("cannot devide by zero")
        else:
            print ("the result is",num1 / num2) 
    case _:
        print ("Invalid operator.")     



