"""Task 1 :
calculator
"""


def operation():
    if operator == "+" :
        
        result = number2 +number1
        print(result)
    
    
    elif operator == "-" : 
        result = number2 - number1
        print(result)
    
    
    elif operator == "/" :
        result =number2 / number1
        print(result)
    

    elif operator == "*":
       result = number1 * number2
       print(result)

try:
  number1 = float(input("enter a number:"))
  number2 = float(input("enter a number:"))
  operator = input("Enter the desired operator (+ - / *):")
        
  operation()   


except ValueError:
    print("please enter your number:")

except ZeroDivisionError:
    print("Division by zero is not allowed.") 
    