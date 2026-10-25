#На вході програми маємо послідовність цілих чисел, що закінчується числом 0.
#Потрібно знайти суму даної послідовності, не враховуючи останнього нуля.
sumNumbers = 0
length = 0
number = int(input(f"Введіть {length+1}-е число: "))
while number != 0:
    sumNumbers += number
    length += 1
    number = int(input(f"Введіть {length+1}-е число: "))
print(f"Сума послідовності: {sumNumbers}")