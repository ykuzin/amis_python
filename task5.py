"""
Умова: Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:

 	
The next number for the number 179 is 180.
The previous number for the number 179 is 178.

Вхідні дані: ціле число

Вихідні дані: два рядки за наведеним у завдання форматом.
"""
# Програма виводить попереднє і наступне числа для введеного.Конструкція 
#try-except перевіряє на правильність тип введеної користувачем інформації.
try:
    numb = int(input("Введіть ціле число "))
    print("The next number for the number %d is %d." % (numb , numb+1))
    print("The previous number for the number %d is %d." % (numb , numb-1))
except ValueError:
    print("Не коректне значення") 
