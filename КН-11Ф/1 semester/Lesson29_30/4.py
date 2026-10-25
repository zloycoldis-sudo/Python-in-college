naturalNum = int(input())
numberPow = 1
count = 0
while pow(2,numberPow) <= naturalNum:
    count += 1
    numberPow += 1
print(count)