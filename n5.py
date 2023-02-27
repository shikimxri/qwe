print("ax^2 + bx + c")

a = int(input("Введите старший коэффициент"))
b = int(input("Введите второй коэффициент"))
c = int(input("Введите свободный коэффициент"))

print("D = b**2-4ac")
print(f'D = {b}**2 -4 * {a} * {c}')

D = (b**2 - 4 * a * c)

print(("D = "), int(D))

if D == 0:
    print("x = −b/2a = ", -b / 2 * a)
elif D > 0:
    print("x1 = -b+sqrt D/2a = ", round(-b + D ** 0.5) / (2 * a))
    print("x2 = -b-sqrt D/2a = ", round(-b - D ** 0.5) / (2 * a))
else:
    print("Нет решений")








