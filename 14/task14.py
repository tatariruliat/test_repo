#print(hex(4 ** 2020 + 2 ** 2017 - 15).count('1'))

#x = 64**10 + 2**90 - 16
#print( oct(x).count('7') )


x = 64**10 + 2**90 - 16
k = 0
while x > 0:
		if x % 9 == 8:#8 - это последняя цифра в 9-ричной сис., тут мы
			k += 1 #берём следующее число и тоже его делим
		x //= 9
print(k)