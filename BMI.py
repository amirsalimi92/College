print('\n')
print('------------------------------------------')
print('IS321 BMI Aufgabe')
print('\n')


print('How to find your weight in kg? \n')
print('https://www.google.com/search?q=pound+to+kg&oq=pound+to+kg&aqs=chrome..69i57j0i512j0i22i30l8.3116j0j7&sourceid=chrome&ie=UTF-8 \n')
weight = float(input('Please insert your weight in kg: \n\n'))


print('How to find your height in cm? \n')
print('https://www.google.com/search?q=foot+to+cm&sxsrf=ALiCzsYn0ZCZZU9aRAN0t9ixurUa3YwxQw%3A1671000749028&ei=rXKZY86uAYqVkgW6hrWQBw&ved=0ahUKEwiOucLwwvj7AhWKiqQKHTpDDXIQ4dUDCA8&uact=5&oq=foot+to+cm&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECAAQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCCMQ6gIQJzoMCAAQ6gIQtAIQQxgBOgQIIxAnOgYIIxAnEBM6CwguEIAEEMcBENEDOgoILhDHARDRAxBDOgoILhCHAhCABBAUOgcIABDJAxBDOgcILhDUAhBDOgsILhCABBDHARCvAToHCAAQgAQQCkoECEEYAEoECEYYAVCICFjSJWC-KmgBcAF4AIABVYgB_gSSAQIxMJgBAKABAbABFMABAdoBBggBEAEYAQ&sclient=gws-wiz-serp \n')
height = float(input('Please insert your height in cm: \n'))


def bmi(weight, height):
    numBmi = weight / ((height/100)**2)
    return numBmi

def info(input):
    if (input < 18.5):
        print('Untergewicht')
    elif (18.5 <= input <= 25):
        print('Normalgewicht')
    elif (25 < input <30):
        print('Übergewicht')
    else:
        print('Adipositas!')


try:
    output = bmi(weight, height)
    print(output)
    print('\n')
    info(output)
except ValueError:
    print('Please insert the valid values')
    output = bmi(weight, height)
    print(output)
    print('\n')
    info(output)
finally:
    again = str(input('Again? (Y for yes/ n for no: '))
    if (again == 'y'):
        output = bmi(weight, height)
        print(output)
        print('\n')
        info(output)
    elif (again == 'n'):
        print('\n')
        print('***** Good Luck *****')
        exit()


