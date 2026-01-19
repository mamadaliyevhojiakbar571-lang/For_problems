# For11. n butun soni berilgan (n > 0). Quyidagi yig'indini hisoblovchi programma tuzilsin.
# S= n? +(n+1)+(n+2)2+... (2*n)?
n = int(input("n = "))
s = 0
for i in range(n, 2*n + 1):
    s += i**2
print("S =", s)