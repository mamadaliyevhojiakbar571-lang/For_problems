# For13. n butun soni berilgan (n > 0). Quyidagi yig'indini hisoblovchi programma tuzilsin.
# S = 1.1 - 1.2 + 1.3 -...
# (nta qo'shiluvchi, ishoralar almashib keladi. Shart operatordan oydalamang)
n = int(input("n = "))
s = 0
for i in range(1, n + 1):
    s += ((-1)**(i+1)) * (1 + i/10)
print("S =", s)