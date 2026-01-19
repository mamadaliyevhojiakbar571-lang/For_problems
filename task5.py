# For5. Bir kg konfetning narxi berilgan (haqiqiy son). 0.1, 0.2, ..., 0.9, 1 kg konfetni narxini chiqaruvchi
# programma tuzilsin.
kg = float(input("kg ni kiriting: "))
for i in range(1, 10):
    weight = i / 10
    print(weight, "kg konfet narxi:", weight * kg)