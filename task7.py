# ---------------
"""
Умова: Нехай число N - кількість хвилин, відрахованих після півночі.
Скільки годин і хвилин буде показувати цифровий годинник, якщо за відлік взяти 00:00?

Програма повинна виводити два числа: кількість годин (від 0 до 23) і кількість хвилин
(від 0 до 59). Візьміть до уваги, що починаючи з півночі може пройти декілька днів,
тому число N може бути достатньо великим.

Вхідні дані: 1 ціле число, що вводить користувач

Вихідні дані: вивести два числа. Перше - години, друге - хвилини.
"""

N=int(input() #Вводимо число хвилин
days=N//(60*24) #Шукаємо число годин, яке буде не перевищувати 24год
print(days//60) #Вивід годин
print(days%60) #Вивід хвилин