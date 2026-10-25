#Дано натуральне число n. Вивести в порядку зростання всі непарні натуральні числа менші n.
number = int(input())
i = 1
while True:
    if i >= number:
        break
    print(i, end=" ")
    i += 2