# 5.Прибавить 5
#Прибавить 2
#Умножить на 2
# Первая из них увеличивает число на экране на 5, вторая увеличивает его на 2, третья умножает его на 2.
# Программа для исполнителя А16 – это последовательность команд.
# Сколько существует таких программ, которые исходное число 3 преобразуют в число 12 и при этом
# траектория вычислений программы содержит число 10?
# def k(x,y):
#     if x > y:
#         return 0
#     if x == y:
#         return 1
#     if y % 2 == 0:
#         return k(x, y-1) + k(x, y-2) + k(x, y // 2)
#     return k(x, y - 1) + k(x, y - 2)
# print(k(3, 10) * k(10, 12))

# a = [0] * 46
# a[8] = 1
# for i in range(9, 46):
#     a[i] = a[i-2] + a[i-10]
#     if i % 2 != 0:
#         a[i] += a[(i+1)//2]
# print(a[45])
