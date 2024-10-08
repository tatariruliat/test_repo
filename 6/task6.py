# Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный момент Черепаха
# находится в начале координат, её голова направлена вдоль положительного направления оси ординат, хвост опущен.
# При опущенном хвосте Черепаха оставляет на поле след в виде линии. В каждый конкретный момент известно положение
# исполнителя и направление его движения. У исполнителя существует две команды: Вперёд n (где n—целое число),
# вызывающая передвижение Черепахи на n единиц в том направлении, куда указывает её голова, и Направо m
# (где m— целое число), вызывающая изменение направления движения на m градусов по часовой стрелке.
# Запись Повтори k [Команда1 Команда2 … КомандаS] означает, что последовательность из S команд повторится k раз.
# Черепахе был дан для исполнения следующий алгоритм: Повтори 7 [Вперёд 10 Направо 120].
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией,
# заданной данным алгоритмом. Точки на линии учитывать не следует.
# from turtle import *
# tracer(0)
# left(90)
# k = 30
# for i in range(7):
#     forward(10*k)
#     right(120)
# pu()
# for x in range(-k, k):
#     for y in range(-k, k):
#         goto(x * k, y * k)
#         dot(5)
# done()

##2. Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный момент Черепаха находится
# в начале координат, её голова направлена вдоль положительного направления оси ординат, хвост опущен.
# При опущенном хвосте Черепаха оставляет на поле след в виде линии. В каждый конкретный момент известно положение исполнителя
# его движения. У исполнителя существует две команды: Вперёд n (где n— целое число), вызывающая передвижение Черепахи
# на n единиц в том направлении, куда указывает её голова, и Направо m (где m— целое число), вызывающая изменение
# направления движения на m градусов по часовой стрелке. Запись
# Повтори k [Команда1 Команда2 … КомандаS]
# означает, что последовательность из S команд повторится k раз. Черепахе был дан для исполнения следующий алгоритм:
# Повтори 5 [Вперёд 9 Направо 120]
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией,
# заданной данным алгоритмом. Точки на линии учитывать не следует.
# from turtle import *
# tracer(0)
# left(90)
# k = 30
# for i in range(5):
#     forward(9*k)
#     right(120)
# pu()
# for x in range(-k, k):
#     for y in range(-k, k):
#         goto(x * k, y * k)
#         dot(5)
# done()
##10. Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный момент Черепаха находится в начале координат,
# её голова направлена вдоль положительного направления оси ординат, хвост опущен. При опущенном хвосте Черепаха оставляет на поле след
# в виде линии. В каждый конкретный момент известно положение исполнителя и направление его движения. У исполнителя существует две команды:
# Вперёд n (где n— целое число), вызывающая передвижение Черепахи на n единиц в том направлении, куда указывает её голова, и Направо m
# (где m— целое число), вызывающая изменение направления движения на m градусов по часовой стрелке. Запись
# Повтори k [Команда1 Команда2 … КомандаS]
# означает, что последовательность из S команд повторится k раз. Черепахе был дан для исполнения следующий алгоритм:
# Повтори 4 [Вперёд 9 Направо 90 Вперёд 7 Направо 90]
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией,
# заданной данным алгоритмом. Точки на линии учитывать не следует.
# from turtle import *
# tracer(0)
# left(90)
# k = 30
# for i in range(4):
#     forward(9*k)
#     right(90)
#     forward(7*k)
#     right(90)
# pu()
# for x in range(-k, k):
#     for y in range(-k, k):
#         goto(x * k, y * k)
#         dot(5)
# done()

##35. Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный момент Черепаха находится в начале координат,
# её голова направлена вдоль положительного направления оси ординат, хвост опущен. При опущенном хвосте Черепаха оставляет на поле след
# в виде линии. В каждый конкретный момент известно положение исполнителя и направление его движения. У исполнителя существует две команды:
# Вперёд n (где n—целое число), вызывающая передвижение Черепахи на n единиц в том направлении, куда указывает её голова;
# Направо m (где m— целое число), вызывающая изменение направления движения на m градусов по часовой стрелке.
# Запись Повтори k [Команда1 Команда2 … КомандаS] означает, что последовательность из S команд повторится k раз (где k— целое число).
# Черепахе был дан для исполнения следующий алгоритм:
# Направо 45 Повтори 7 [Вперёд 5 Направо 45 Вперёд 10 Направо 135].
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, которая ограничена линией, заданной алгоритмом.
# Точки на линии учитывать не следует.
# from turtle import *
# tracer(0)
# left(90)
# right(45)
# k = 30
# for i in range(7):
#     forward(5 * k)
#     right(45)
#     forward(10 * k)
#     right(135)
# pu()
# for x in range(-k, k):
#     for y in range(-k, k):
#         goto(x * k, y * k)
#         dot(5)
# done()

# string = "hello world"
# for char in string:
#     print(char)



from turtle import *
k =20
tracer(0)
right(90)
for i in range(11):
    for u in range(4):
        forward(10)
        right(90)
        forward(10)
        right(270)
    right(90)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
done()