#Задано натуральне число n. Змоделюйте зворотній відрахунок таймера від n до 0 як наведено у прикладі
while True:
    countdown = int(input())
    if countdown < 0:
        continue
    for i in range(countdown, 0 - 1, -1):
        print(f"{i} sec.")
    break