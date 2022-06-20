from typing import final

from numpy import char


print('\n')
print('------------------------------------------')
print('IS321 Calculator Aufgabe')
print('\n')

def calculator():
    first = float(input('Please insert the first number: '))
    second = float(input('Please insert the second number: '))
    print('\n')

    operator = str(input('Please insert\n+ for sum\n- for subtract\n* for multiply\n/ for divide\n** for power: '))

    if (operator == '+'):
        result = first+second
    elif (operator == '-'):
        result = first-second
    elif (operator == '*'):
        result = first*second
    elif (operator == '/'):
        result = first/second
    elif (operator == "**"):
        result = first ** second
    else:
        print('please choose a correct symbol')

    print('\n')
    print('Result is : '+ str(result))
    print('\n')
    print('\n')
    print('------------------------------------------')
    print('\n')

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
