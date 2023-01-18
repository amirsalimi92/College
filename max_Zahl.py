numbers = [-5,-2,-1]
max = 0

for i in range(3):
    max = numbers[i]
    if (numbers[i] > max):
        max = numbers[i]

print(max)