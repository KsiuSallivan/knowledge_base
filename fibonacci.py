# Неверное решение из головы
# def fibo0(num):
#     list_num = [0, 1]
#     for i in range(2, num + 1):
#         x = (i - 2) + (i - 1)
#         list_num.append(x)
#     return list_num
#

def fibo1(num):
    list_num = [0, 1]
    for i in range(2, num):
        x = list_num[i - 1] + list_num[i - 2]  # Используем значения из списка
        list_num.append(x)
    return list_num


def fibo2(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]


def fibo3(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


print(fibo1(25))
print(fibo2(25))
print(fibo3(25))