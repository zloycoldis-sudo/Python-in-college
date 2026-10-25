#Для натурального числа n вивести всі степені двійки менші за n
number = int(input())
power = 2
while True:
    if power >= number:
        break
    print(power, end=" ")
    power *= 2