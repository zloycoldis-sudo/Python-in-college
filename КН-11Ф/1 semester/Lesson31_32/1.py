#Задано натуральне число n. Порахуйте і виведіть повідомлення OK як показано у прикладі.
while True:
    limit = int(input())
    if limit < 0:
        continue
    for i in range(limit):
        print(f"{i + 1} OK")
    break