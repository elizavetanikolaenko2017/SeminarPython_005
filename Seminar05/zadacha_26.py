"""
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
"""
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
def degree_numbers(a,b):
    if a==0:
        return b
    return a* pow(a,b-1)
print(f"Степень данного числа: {degree_numbers(a,b)}")





