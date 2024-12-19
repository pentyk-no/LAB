n = int(input("Введите длину массива: "))

num = []
i = 0
suma = 0
umn = 1
while i < n:
    num.append(int(input("Введите элемент массива: ")))
    i+=1
for el in num:
    if el % 2 == 0:
        suma += el
    else:
        umn *= el
        
print("Сумма четных:", suma)
print("Умножение нечетных:", umn)
        
        



