"""
Умова: Нехай число N - кількість хвилин, відрахованих після півночі. Скільки годин і хвилин буде показувати цифровий годинник, якщо за відлік взяти 00:00?

Програма повинна виводити два числа: кількість годин (від 0 до 23) і кількість хвилин (від 0 до 59). Візьміть до уваги, що починаючи з півночі може пройти декілька днів, тому число N може бути достатньо великим.

Вхідні дані: 1 ціле число, що вводить користувач

Вихідні дані: вивести два числа. Перше - години, друге - хвилини.

"""
#Програма обчислює скільки годин і хвилин буде показувати цифровий годинник, якщо за відлік взяти 00:00
##Конструкція try-except перевіряє на правильність тип введеної користувачем інформації.
try:
    minutes = int(input("Введіть кількість хвилин "))
    while(minutes > 24*60):
        minutes -= 24*60
    hours = minutes//60
    minu = minutes - hours*60 
    print("Годин - %d Хвилин - %d" % (hours , minutes)) 
except ValueError :
    print("Ви ввели некоректну кількість годин")
