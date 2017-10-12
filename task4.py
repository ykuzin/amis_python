"""

Умова: N студентів отримали K яблук і розподілити їх між собою порівну. 
Неподілені яблука залишились у кошику. Скільки яблук отримає кожен студент? 
Скільки яблук залишиться в кошику?

Програма отримує числа N і K. Вона повинна вивести два числа: відповіді на 
поставлені вище питання.

Вхідні дані: 2 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести два числа. Перше - кількість яблук у студента, друге - 
кількість яблук, що лишилось у кошику.
"""
# Програма для підрахунка кількості яблук для кожного і остачі.Конструкція виключень оброблює випадки 
#ділення на нуль і введння неправильного значення, при введенні відємного значення береться його модуль.
try:
    students = abs(int(input("ВВедіть кількість студентів ")))
    apples = abs(int(input("Введіть кількість яблук ")))
    koshik = apples % students
    nn = apples // students
    print("Кількість яблук у студента %d кількість яблук в кошику %d" %  (nn , koshik))
except (ZeroDivisionError , ValueError):
    print("Ви ввели не число або нуль в кількість студентів")