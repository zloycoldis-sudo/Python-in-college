iterator = int(input())
number = 1
while iterator >0:
    if number > iterator:
        break
    if (number % 2 != 0) and (number % 3 != 0) and (number % 5 != 0):
        print(number, end=" ")
        number += 1