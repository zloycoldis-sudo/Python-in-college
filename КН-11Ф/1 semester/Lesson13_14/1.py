#Вивести 1, якщо будинки з номерами n і m знаходяться на одній стороні вулиці, і 0 у протилежному випадку.
n, m = map(int, input('Enter house numbers: ').split())
if (n + m) % 2 == 0:
    print(1)
else:
    print(0)