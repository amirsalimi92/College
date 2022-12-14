print('\n')
print('------------------------------------------')
print('IS321 Calculator Aufgabe')
print('\n')

def calculate():
    counter = 0
    summ = 0
    temp = []
    while (counter<6):
        temp.append(float(input('Insert the {}. temperature: '.format(counter))))
        counter += 1
    
    for number in temp:
        summ += number

    avg = summ / 6

    print('Average is: ')
    print(avg)


try:
    calculate()
except ValueError:
    print('Please insert the valid values')
    calculate()
finally:
    again = str(input('Again? (Y for yes/ n for no: '))
    if (again == 'y'):
        calculate()
    elif (again == 'n'):
        print('\n')
        print('***** Good Luck *****')
        exit()