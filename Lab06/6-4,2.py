n = int(input("Введите длину массива: "))
num = []
i = 0
while i < n:
    num.append(int(input("Введите элемент массива: ")))
    i+=1
min_index = num.index(min(num))
max_index = num.index(max(num))
num[min_index], num[max_index] = num[max_index], num[min_index]
print(num)
