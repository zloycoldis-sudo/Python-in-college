#Увести три цілих числа коофіцієнти a,b,c квадратного рівняння.
#Визначте кількість коренів рівняння.
a, b, c = map(int, input('Enter the three coefficients.').split())
discriminant = pow(b,2) - 4*a*c
if discriminant > 0:
    print('The equation has two real roots.')
elif discriminant == 0:
    print('The equation has one real root.')
else:
    print('The equation has not real roots.')