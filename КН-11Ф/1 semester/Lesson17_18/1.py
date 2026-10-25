#Потрібно порахувати скільки років дитині, якщо відомо дату народження та поточну дату.
import datetime
dd, mm, yyyy = input("Введіть дату народження через пробіл (день місяць рік): ").split()
today = datetime.date.today()
if (int(dd) < 1 or int(dd) > 31) or (int(mm) < 1 or int(mm) > 12) or (int(yyyy) < 1900 or int(yyyy) > today.year):
    print("Неправильний формат дати")
    exit()
age = today.year - int(yyyy)
if (today.month, today.day) < (int(mm), int(dd)):
    age -= 1 
print(f"Вік дитини: {age} років")