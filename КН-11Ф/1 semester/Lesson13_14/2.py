#Дано невід'ємне ціле число.
#Перевірити, чи ділиться воно на 2, на 4 та на 8.
number = abs(int(input('Enter a number: ')))
if number % 2 == 0:
    print('YES')
else:
    print('NO')
if number % 4 == 0:
    print('YES')
else:
    print('NO')
if number % 8 == 0:
    print('YES')
else:
    print('NO')