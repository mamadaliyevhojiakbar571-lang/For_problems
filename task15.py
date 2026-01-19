# For15. n butun soni va a haqiqiy soni berilgan (n > 0). a ning n - darajasini aniqlovchi programma
# tuzilsin.
# a'=a*a*a..a;
n = int(input("n = "))
a = float(input("a = "))
natija = 1
for i in range(n):
    natija *= a
print(f"{a} ning {n} - darajasi: {natija}")