#Увести ціле число та визначити,воно доданнє, від'ємне чи нуль.
#Вивести 1 коли воно додатнє, -1 коли від'ємне та 0 коли воно дорівнюює нулю.
number = int(input('Enter a number: '))
if number > 0:
    print('The number id positive.')
elif number < 0:
    print('The number is negative.')
else:
    print('The number is zero.')