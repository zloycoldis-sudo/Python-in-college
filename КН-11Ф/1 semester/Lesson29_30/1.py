inputNum = int(input())
number = 1
while inputNum > 0:
    if pow(number, 2) > pow(inputNum, 2):
        break
    else:
        print(pow(number, 2), end=" ")
        number+=1