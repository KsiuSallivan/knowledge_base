# Неверное решение из головы
# def factorial_0(num):
#     f = 0
#     for i in range(1, num+1):
#         f = i*(i+1) # 1*2*3*4
#     return f


def factorial_1(num):
    f = 1  # Начинаем с 1, так как факториал 0 равен 1
    for i in range(1, num + 1):
        f *= i  # Умножаем f на i для получения факториала
    return f


print(factorial_1(5))


def factorial_2(n):
    # Базовый случай
    if n == 0:
        return 1
    # Рекурсивный случай
    else:
        return n * factorial_2(n - 1)


print(factorial_2(6))