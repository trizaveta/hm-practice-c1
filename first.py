a = float(input("Введите длину первой стороны:"))
b = float(input("Введите длину второй стороны:"))
C = float(input("Ввведите угол между сторонами:"))
import math
C1 = math.radians(C)
def find_third_side (a, b, C1):
    return math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(C1))
result = find_third_side (a, b, C1)
print ("Длина третьей стороны:", result)
