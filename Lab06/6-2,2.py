def find_max_k(n):
    k = 0
    while 2 ** k <= n:
        k += 1
    return k

N = int(input("Введите целое число N (> 1): "))
if N > 1:
    K = find_max_k(N)
    print("Наибольшее целое число K, при котором 2^K > {N}, равно: {K}")
else:    
    print("Введено неверное значение N")

