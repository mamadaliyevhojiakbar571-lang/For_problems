# For9. a va b butun sonlari berilgan (a < b). a dan b gacha bo'lgan barcha butun sonlar kvadratlarining
# yig'indisini chiqaruvchi programma tuzilsin.
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
summa = 0
for i in range(a, b + 1):
    summa += i ** 2
print("Kvadratlar yig'indisi:", summa)