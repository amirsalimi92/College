
print('\n')
print('------------------------------------------')
print('IS321 Calculator Aufgabe OOP')
print('\n')

def calculator():
    first = float(input('Please insert the first number: '))
    second = float(input('Please insert the second number: '))
    print('\n')

    operator = str(input('Please insert\n+ for sum\n- for subtract\n* for multiply\n/ for divide\n** for power: '))

    if (operator == '+'):
        result = plus(first, second)
    elif (operator == '-'):
        result = minus(first, second)
    elif (operator == '*'):
        result = multiple(first, second)
    elif (operator == '/'):
        result = div(first, second)
    elif (operator == "**"):
        result = power(first, second)
    else:
        print('please choose a correct symbol')

    print('\n')
    print('Result is : '+ str(result))
    print('\n')
    print('\n')
    print('------------------------------------------')
    print('\n')

    

def plus(num1, num2):
    result = num1 + num2
    
    return result

def minus(num1, num2):
    result = num1 - num2
    
    return result

def multiple(num1,num2):
    result = num1 * num2
    
    return result

def div(num1,num2):
    result = num1 / num2
    
    return result

def power(num1,num2):
    result = num1 ** num2
    
    return result
  

try:
    calculator()
except ValueError:
    print('Please insert the valid values')
    calculator()
finally:
    again = str(input('Again? (Y for yes/ n for no: '))
    if (again == 'y'):
        calculator()
    elif (again == 'n'):
        print('\n')
        print('***** Good Luck *****')
        exit()
