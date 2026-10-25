#Напишіть програму, що порахує суму послідовності яка містить п'ять чисел або закінчується 0, якщо чисел в послідовності менше.
number = int(input())
suma_numbers = number
n = 1
while number != 0 and n < 5:
    number = int(input())
    suma_numbers += number
    n += 1
print(suma_numbers)