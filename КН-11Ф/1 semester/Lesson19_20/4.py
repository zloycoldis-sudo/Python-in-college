#На вході програми маємо три натуральних числа a, b і c, записані в одному рядку через пропуск.
#У відповідь потрібно вивести одне з повідомлень:
#– equilateral, якщо існує рівносторонній трикутник з довжинами сторін a, b, c;
#– isosceles, якщо існує рівнобедрений трикутник з довжинами сторін a, b, c;
#– versatile, якщо існує різносторонній трикутник з довжинами сторін a, b, c;
#– invalid, якщо трикутника з довжинами сторін a, b, c не існує.
while True:
    print("\033[H\033[J", end="")
    a, b, c = map(float, input('Вкажіть сторінки трикутника(m): ').split())
    if (a <= 0 or b <= 0 or c <= 0):
        print('Сторони трикутника повинні бути натуральними числами.')
        continue
    if a + b <= c or a + c <= b or b + c <= a:
        print('invalid')
        break
    elif a == b and a == c and b == c:
        print('equilateral')
        break
    elif a ==b or a == c or b == c:
        print('isosceles')
        break
    elif a != b and a != c and b != c:
        print('versatile')
        break