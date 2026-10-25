#Дано три різні числа a, b, c. Вивести середнє з них.
a, b, c = map(int, input("Введіть три різні числа через пробіл: ").split())
numbers = sorted([a, b, c])
print(f"Середнє з них: {numbers[1]}")