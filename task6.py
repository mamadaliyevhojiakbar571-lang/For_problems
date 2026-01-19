# For6. Bir kg konfetning narxi berilgan (haqiqiy son). 1.2, 1.4, ... 2 kg konfetni narxini chiqaruvchi
# programma tuzilsin.
kg = float(input("kg ni kiriting: "))
for i in range(12, 21, 2):
    weight = i / 10
    print(weight, "kg konfet narxi:", weight * kg)