# For19. n butun soni berilgan (n > 0). Birdan n gacha bo'lgan sonlar ko'paytmasini chiqaruvchi
# programma tuzilsin. n! =1*2*…n
# Birdan n gacha bo'lgan sonlar ko'paytmasi n faktorial deyiladi.
n = int(input("n = "))
s = 1
for i in range(1, n + 1):
    s *= i
print(f"1 dan {n} gacha bo'lgan sonlar ko'paytmasi (n!) =", s)
