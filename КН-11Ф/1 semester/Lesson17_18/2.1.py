#Дано три різні числа a, b, c. Вивести середнє з них.
a, b, c = map(int, input("Введіть три різні числа через пробіл: ").split())
if a == b == c:
    print("Середнє з них рівне себе")
elif (a > b > c) or (c > b > a):
    print(f"Середнє з них: {b}")
elif (b > a > c) or (c > a > b):
    print(f"Середнє з них: {a}")
elif (a > c > b) or (b > c > a):
    print(f"Середнє з них: {c}")