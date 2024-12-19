str = input ("Введите строку ")
for w in str.split():
    if(w.startswith("а") or w.endswith("я")): 
        print(w)
