# For3. a va b butun sonlan berilgan (a < b). a va b sonlari orasidagi barcha butun sonlami (a va b dan
# tashqari) kamayish tartibida chiqaruvchi va chiqarilgan sonlar sonini chiqaruvchi progma tuzilsin.
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
count = 0
for i in range(b - 1, a, -1):
    print(i)
    count += 1
print("Chqarilgan sonlar soni:", count)