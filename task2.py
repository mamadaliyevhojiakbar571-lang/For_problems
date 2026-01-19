# For2. a va b butun sonlari berilgan (a < b). a va b sonlar orasidagi barcha butun sonlami (a va b ni
# ham) chiqaruvchi va chiqarilgan sonlar sonini chiqaruvchi programma tuzilsin. (a va b xam chiqarilsin).
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
count = 0
for i in range(a, b + 1):
    print(i)
    count += 1
print("Chqarilgan sonlar soni:", count)