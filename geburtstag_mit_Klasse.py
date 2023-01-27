class Geburtstag:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

    def nice_print(self):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        monthNumber = int(self.month) - 1
        monthFull = months[monthNumber]
        print(f'{monthFull} {self.day}.{self.year}')

Amir = Geburtstag(18,10,1992)

Geburtstag.nice_print(Amir)
print(Amir)