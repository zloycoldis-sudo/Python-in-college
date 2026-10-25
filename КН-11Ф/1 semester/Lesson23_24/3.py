#На вході програми маємо послідовність цілих чисел, що закінчується числом 0.
#Потрібно знайти кількість від'ємних чисел в даній послідовності.
countNegNums = 0
length = 0
number = int(input(f"Введіть {length+1}-е число: "))
while number != 0:
    if number < 0:
        countNegNums += 1
    length += 1
    number = int(input(f"Введіть {length+1}-е число: "))
print(f"Кількість від'ємних чисел: {countNegNums}")