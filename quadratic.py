import math

a = float(input("a коэффициентін енгізіңіз: "))
b = float(input("b коэффициентін енгізіңіз: "))
c = float(input("c коэффициентін енгізіңіз: "))

D = b**2 - 4*a*c
print(f"Дискриминант: {D}")

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Екі түбір: x1 = {x1:.2f}, x2 = {x2:.2f}")
elif D == 0:
    x = -b / (2*a)
    print(f"Бір ғана түбір: x = {x:.2f}")
else:
    print("Нақты түбірлер жоқ.")
