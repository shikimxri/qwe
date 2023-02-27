print("y=ax^2+bx+c")

a = int(input("Введите старший коэффициент\n"))
b = int(input("Введите второй коэффициент\n"))
c = int(input("Введите свободный коэффициент\n"))

print(f'y={a}x^2{b}x+{c}')

x1 = int(input("Введите х1\n"))
print(f'при x1 = {x1}, y1 = ' , a * x1**2 + b * x1 + c)

x2 = int(input("Введите х2\n"))
print(f'при x2 = {x2}, y2=' , a * x2**2 + b * x2 + c)

x3 = int(input("Введите х3\n"))
print(f'при x1 = {x3}, y3=' , a * x3**2 + b * x3 + c)

x4 = int(input("Введите х4\n"))
print(f'при x4 = {x4}, y4=' , a * x4**2 + b * x4 + c)
