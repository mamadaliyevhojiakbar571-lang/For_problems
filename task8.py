# For8. a va b butun sonlari berilgan (a < b). a dan b gacha bo'lgan barcha butun sonlar ko'paytmasini
# chiqaruvchi programma tuzilsin.
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
kopaytma = 1
for i in range(a, b + 1):
    kopaytma *= i
print("Ko'paytma:", kopaytma)    