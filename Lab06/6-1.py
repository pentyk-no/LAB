h = int(input("Введите значение высоты треугольника: ")) 
a = int(input("Введите значение основания треугольника: "))
S = 1/2 * h * a
print ("Площадь =", S)
if S % 2 == 0:
 S /= 2
 print("Половина площади", S)
else:
 print ("Не могу делить на 2!")
