total = 0
suma = 0
print("Введите числа последовательности оканчивающаяся 0: ")
while True:
    num = int(input())
    if num == 0:
            break
    suma += num
    total += 1
print("Сумма чисел = " , suma)       
print("Количество чисел = ", total + 1)

