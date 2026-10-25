#У деякій школі заняття розпочинаються о 9:00.
#Тривалість уроку - 45 хвилин, після 1-го, 3-го, 5-го і т.д. уроків перерва 5 хвилин, а після 2-го, 4-го, 6-го і т.д. - 15 хвилин.
#Визначте, коли закінчується вказаний урок.
#Вхідні дані: Дано номер уроку (число від 1 до 10).
#Вихідні дані: Виведіть два цілі числа: час закінчення уроку в годинах і хвилинах.
lesson_count = abs(int(input("Введіть номер уроку(від 1 до 10): ")))
total_minutes = lesson_count * 45
breaks_count = lesson_count - 1
small_breaks = breaks_count // 2 + breaks_count % 2 
big_breaks = breaks_count // 2
total_minutes += small_breaks * 5
total_minutes += big_breaks * 15
total_minutes = total_minutes % 1440
print(f"{lesson_count}-й урок закінчується о {total_minutes // 60 + 9}:{total_minutes % 60}")