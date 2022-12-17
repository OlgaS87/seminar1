# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

n = int(input("Input number from 1 to 7: "))
if n < 1 or n > 7:
    print("It's not a day of the week!")
elif n > 5:
    print('Yes')
else:
    print('No')
