class Birthday:
    def print(day,month,year):
        print(f'{day}. {month}. {year}')

    def print_nice(day,month,year):
        changedMonth = int(month) -1
        months = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']
        finalMonth = months[changedMonth]

        print(f'{day}. {finalMonth} {year}')


day = input('Please insert the day of your birthday: ')
month = input('Please insert the month of your birthday: ')
year = input('Please insert the year of your birthday: ')

Birthday.print(day,month,year)
Birthday.print_nice(day,month,year)