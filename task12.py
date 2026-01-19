# For12. n butun soni berilgan (n > 0). Quyidagi ko'paytmani hisoblovchi programma tuzilsin.
# S = 1.1*12 *1.3 *
# (n ta ko'payuvchi)
n = int(input("n = "))
s = 1
for i in range(1, n + 1):
    s *= (1 + i/10)
print("S =", s)