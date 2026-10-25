#Програма на вході приймає натуральне число m. Потрібно знайти кількість натуральних повних квадратів, що не перевищують m.
naturalNumber = int(input())
count = 0
number = 1
while naturalNumber > 0:
    if pow(number, 2) > naturalNumber:
        break
    elif pow(number, 2) <= naturalNumber:
        count += 1
    number += 1
print(count)