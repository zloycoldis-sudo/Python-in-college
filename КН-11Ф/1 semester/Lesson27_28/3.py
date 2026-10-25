#Потрібно знайти і вивести кількість непарних натуральних n-значних чисел, що лежать на відрізку [a,b].
n, a, b = map(int, input().split())
countNegNum = 0
minNum = pow(10, n - 1)
i = minNum
maxNum = pow(10, n) - 1
if a > minNum:
    i = a
while True:
    if i > maxNum or i > b:
        break
    if i % 2 != 0:
        countNegNum += 1
    i += 1
print(countNegNum)