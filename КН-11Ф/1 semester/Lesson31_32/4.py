#Учасникам забігу надали номери від a до b (a ≤ b), цю інформацію занесли до комп'ютера у зворотному порядку.
#Вивести номери спортсменів одним рядком через проміжок в спаданні.
while True:
    firstNum, lastNum = map(int, input().split())
    if firstNum > lastNum or firstNum < 0 or lastNum < 0:
        continue
    for i in range(lastNum, firstNum - 1, -1):
        if i == firstNum:
            print(i)
        else: print(i, end=" ")
    break