a = [] # список для хранения значений А

for A in range(1,200):

k = 1 # флаг

for x in range(1,100):

for y in range(1,100):

if (((x<=9)<=(x*x<=A))and((y*y<=A)<=(y<=9)))==False:

k = 0 # появился Х или Y, при котором ЛОЖЬ

break

if k == 1: # все числа Х и Y перебрали

a.append( A )

print( max(a) )