# For14. n butun soni berilgan (n > 0). Shu sonning kvadratini quyidagi formula asosida hisoblovchi
# programma tuzilsin.
# nº=1 +3+5+ + (2*n - 1)
# har bir qo'shiluvchidan keyin natijani ekranga chiqarib boring. Natijda ekranda 1 dan n gacha bo'lgan
# sonlar kvadratı chiqanladı.
n = int(input("n = "))
s = 0
for i in range(1, n + 1):
    s += (2*i - 1)
    print(f"{i} ning kvadrati: {s}")