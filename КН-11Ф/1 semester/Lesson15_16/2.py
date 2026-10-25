#Увести номер місяця. По номеру місяця визначити пору року.
month = abs(int(input("Введіть номер місяця: ")))
if month in (1, 2, 3):
    print('Зима')
elif month in (3, 4, 5):
    print('Весна')
elif month in (6, 7, 8):
    print('Літо')
elif month in (9, 10, 11):
    print('Весна')
else:
    print('Вкажіть місяць в діапазоні від 1 до 12')