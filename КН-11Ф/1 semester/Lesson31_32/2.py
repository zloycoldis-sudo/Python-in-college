#Учасникам забігу надали номери від a до b та занесли цю інформацію до комп'ютера. Виведіть номери спортсменів.
while True:
    firstNum, lastNum = map(int, input().split())
    if firstNum > lastNum or firstNum < 0 or lastNum < 0:
        continue
    for i in range(firstNum, lastNum + 1):
        if i == lastNum:
            print(i)
        else: print(i, end=" ")
    break