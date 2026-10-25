naturalNum = int(input())
count = 0
if naturalNum == 0:
    count = 1
else:
    while naturalNum > 0:
        naturalNum //= 10
        count += 1
print(count)