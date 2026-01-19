# For20. n butun soni berilgan (n > 0). Bir sikldan foydalangan holda quyidagi yig'indini hisoblovchi
# programma tuzilsin.
# 1! + 2! + 3! +…. +n!
n = int(input("n butun sonini kiriting: "))

yigindi = 0
faktorial = 1

for i in range(1, n + 1):
    faktorial *= i     
    yigindi += faktorial 
    print(f"{i}! = {faktorial}") 

print(f"Barcha faktoriallar yig'indisi: {yigindi}")