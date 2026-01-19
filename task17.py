# For17. n butun soni va a haqiqiy soni benlgan (n > 0). Bır sikldan foydalanıb quyidagi a ning 1 dan n
# gacha bo'lgan barcha darajalarini chiqaruvchi va yig'indini hisoblovchi programma tuzilsin.
# 1+ a+ a2+ a3 +..a"
a = float(input("a = "))
n = int(input("n = "))

s = 1.0     
daraja = 1.0 

print(f"a^0 = 1") 

for i in range(1, n + 1):
    daraja *= a      
    s += daraja      
    print(f"a^{i} = {daraja}")

print("-" * 20)
print(f"Jami yig'indi: {s}")