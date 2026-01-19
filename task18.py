# For18. n butun soni va a hagiqiy soni benlgan (n > 0). Bir sikldan foydalanib quyidagi a ning 1 dan n
# gacha bo'lgan barcha darajalarini chiqaruvchi va yig'indini hisoblovchi programma tuzilsin.
# 1-a+ a2-a3+... (-1)" an
# Shart operatoridan foydalanilmasin.
a = float(input("a = "))
n = int(input("n = "))

s = 1.0
daraja = 1.0

for i in range(1, n + 1):
    daraja *= (-a)  
    s += daraja
    print(f"(-a)^{i} natijasi: {daraja}")

print(f"Yakuniy natija: {s}")
