# Comparação a multiplicação de 2 matrizes 2x2
# utilizando força bruta e fast matrix multiplication

import numpy
from time import time
from random import randint

def matrix_multiplication_2x2(A, B, return_exec_time=True):
	start = time()

	Cline1 = []
	Cline2 = []
	
	Cline1.append((A[0][0] * B[0][0]) + (A[0][1] * B[1][0]))
	Cline1.append((A[0][0] * B[0][1]) + (A[0][1] * B[1][1]))
	Cline2.append((A[1][0] * B[0][0]) + (A[1][1] * B[1][0]))
	Cline2.append((A[1][0] * B[0][1]) + (A[1][1] * B[1][1]))

	C = numpy.matrix([Cline1, Cline2])

	finish = time()
	execution_time = finish - start

	if return_exec_time:
		return C, execution_time

	else:
		return C

def fast_matrix_multiplication_2x2(A, B, return_exec_time=True):
	start = time()

	Cline1 = []
	Cline2 = []

	p1 = A[0][0] * (B[0][1] - B[1][1])
	p2 = B[1][1] * (A[0][0] + A[0][1])
	p3 = B[0][0] * (A[1][0] + A[1][1])
	p4 = A[1][1] * (B[1][0] - B[0][0])
	p5 = (A[0][0] + A[1][1]) * (B[0][0] + B[1][1])
	p6 = (A[0][1] - A[1][1]) * (B[1][0] + B[1][1])
	p7 = (A[0][0] - A[1][0]) * (B[0][0] + B[0][1])

	Cline1.append(p5 + p4 - p2 + p6)
	Cline1.append(p1 + p2)
	Cline2.append(p3 + p4)
	Cline2.append(p5 + p1 - p3 - p7)

	C = numpy.matrix([Cline1, Cline2])

	finish = time()
	execution_time = finish - start

	if return_exec_time:
		return C, execution_time
	else:
		return C

def random_2x2_matrix():
	mline1 = []
	mline2 = []

	mline1.append(randint(-10, 10))
	mline1.append(randint(-10, 10))
	mline2.append(randint(-10, 10))
	mline2.append(randint(-10, 10))

	matrix = [mline1, mline2]

	return matrix

A = random_2x2_matrix()
B = random_2x2_matrix()

brute_force, brute_force_time = matrix_multiplication_2x2(A, B)
fast_matrix, fast_matrix_time = fast_matrix_multiplication_2x2(A, B)

print("A: ")
print(A,"\n")

print("B: ")
print(B,"\n")

print("Força bruta: ")
print(brute_force,"\n")

print("Fast matrix:")
print(fast_matrix,"\n")

print("Força bruta executa em {} segundos".format(brute_force_time))
print("Fast matrix executa em {} segundos".format(fast_matrix_time))