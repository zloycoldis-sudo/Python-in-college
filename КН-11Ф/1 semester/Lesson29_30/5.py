num1, num2 = map(int, input().split())
countPow = 0
numberPow = 1
while pow(2, numberPow) <= num2:
    if pow(2, numberPow) >= num1:
        countPow +=1
    numberPow +=1
print(countPow)