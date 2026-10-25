n, m = map(int, input().split())
count = 0
minN = pow(10, n - 1)
i = minN
maxN = pow(10, n) - 1
while n > 0 and m > 0:
    if i > maxN:
        break
    if i % 2 != 0:
        count += 1
    i += 1