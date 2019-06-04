from random import randint

def split(lista):
	size = len(lista)
	left, right = [], []

	i = 0
	while i < size:
		if i < size/2:
			left.append(lista[i])
		else:
			right.append(lista[i])
		i += 1

	return left, right

def zip(left, right):
	size_l = len(left)
	size_r = len(right)
	total = []

	i = 0
	while i < size_l:
		total.append(left[i])	
		i += 1

	i = 0
	while i < size_l:
		total.append(right[i])	
		i += 1

	return total

def random_list(size):
	lista = []

	i = 0
	while i < size:
		num = randint(0,size)
		if num not in lista:
			lista.append(num)
			i += 1

	return lista

# código adaptado de http://www.codcad.com/lesson/37
INF = 1000000000
def counting_inversions(v):
	inv = 0

	if len(v) == 1:
		return 0

	u1, u2 = split(v)
	inv += counting_inversions(u1)
	inv += counting_inversions(u2)

	u1.append(INF)
	u2.append(INF)
	
	i, ini1, ini2 = 0, 0, 0

	while i < len(v):
		if(u1[ini1] <= u2[ini2]):
			v[i] = u1[ini1]
			ini1 += 1

		else:
			v[i] = u2[ini2]
			ini2 += 1

			inv += len(u1)-ini1-1

		i += 1

	return inv

lista = random_list(size=15)
print('lista = ', lista)
print('inversões = ', counting_inversions(lista))