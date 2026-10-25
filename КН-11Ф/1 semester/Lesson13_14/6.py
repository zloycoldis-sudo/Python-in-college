#Дано натуральне число N (1 ≤ N ≤ 100), яке визначає вік людини.
#Виведіть це число з відповідним доданком rik, roki, rokiv. Наприклад, 1 rik, 12 rokiv, 94 roki.
N = int(input('Enter age (1-100): '))

if N < 1 or N > 100:
    print('The age is out of range.')
    exit()

if N % 10 == 1 and N % 100 != 11:
    print(f'{N} rik')
elif 2 <= N % 10 <= 4 and N % 100 !=12:
    print(f'{N} roki')
else:
    print(f'{N} rokiv')