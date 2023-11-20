import sys

def input_coefficient(prompt):
    while True:
        try:
            coefficient = float(input(prompt))
            return coefficient
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите действительное число.")

def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

def calculate_roots(a, b, discriminant):
    if a == 0:
        raise ValueError("Коэффициент 'a' не может быть равен нулю для квадратного уравнения.")

    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x,
    else:
        return None

if __name__ == "__main__":
    # Проверка наличия параметров командной строки
    if len(sys.argv) == 4:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(sys.argv[3])
        except ValueError:
            print("Некорректные коэффициенты. Пожалуйста, введите действительные числа.")
            sys.exit(1)
    else:
        print("Введите коэффициенты уравнения:")
        a = input_coefficient("Коэффициент A: ")

        while a == 0:
            print("Коэффициент 'a' не может быть равен нулю для квадратного уравнения.")
            a = input_coefficient("Коэффициент A: ")

        b = input_coefficient("Коэффициент B: ")
        c = input_coefficient("Коэффициент C: ")

    discriminant = calculate_discriminant(a, b, c)

    if discriminant >= 0:
        roots = calculate_roots(a, b, discriminant)
        print("Дискриминант:", discriminant)
        print("Корни уравнения:", roots)
    else:
        print("Уравнение не имеет действительных корней.")
