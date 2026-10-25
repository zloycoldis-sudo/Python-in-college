#На вході програми маємо два цілих числа a і b (a < b), записані в одному рядку через пропуск.
#Потрібно вивести всі цілі парні числа, що належать інтервалу [a,b] - в одному рядку, через проміжок і в спадному порядку
firstNum, lastNum = map(int, input().split())
if firstNum < lastNum:
    temporaryVar = firstNum
    firstNum = lastNum
    lastNum = temporaryVar
if firstNum % 2 != 0:
    startRange = firstNum - 1
else:
    startRange = firstNum
for i in range(startRange, lastNum - 1, -2):
    if i == lastNum: print(i)
    else: print(i, end=" ")