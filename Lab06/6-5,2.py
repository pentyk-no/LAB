def find_min_recursive(arr, n):    
    if n == 1:
        return arr[0]        
    min_of_rest = find_min_recursive(arr, n - 1)        
    return min(arr[n - 1], min_of_rest)
n = int(input("Введите длину массива: "))
arr = []
i = 0
while i < n:
    arr.append(int(input("Введите элемент массива: ")))
    i+=1
result = find_min_recursive(arr, n)
print(f"Минимальный элемент массива: {result}")



