# For16. n butun sonı va a hagııy sonı benlgan (n > 0). Bır sıkidan toydalanıb a ning 1 dan n gacha
# bo'lgan barcha darajalarini chiqaruvchi programma tuzilsin.
n = int(input("n = "))
a = float(input("a = "))
for i in range(1, n + 1):
    daraja = 1
    for j in range(i):
        daraja *= a
    print(f"{a} ning {i} - darajasi: {daraja}")