# Неверное решение из головы
# def factorial_0(num):
#     f = 0
#     for i in range(1, num+1):
#         f = i*(i+1) # 1*2*3*4
#     return f


def factorial(num):
    f = 1  # Начинаем с 1, так как факториал 0 равен 1
    for i in range(1, num + 1):
        f *= i  # Умножаем f на i для получения факториала
    return f


print(factorial(5))