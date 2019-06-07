from random import randint
from time import time

def merge_sort(array):

    if len(array) > 1:
        middle = int(len(array)/2)
        left_array = array[:middle]
        right_array = array[middle:]

        merge_sort(left_array)
        merge_sort(right_array)

        i, j, k = 0, 0, 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k]=left_array[i]
                i += 1
            else:
                array[k]=right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            array[k]=left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k]=right_array[j]
            j += 1
            k += 1

vetor = []
num = 100000
for i in range(num):
    vetor.append(randint(0,num))

inicio = time()
merge_sort(vetor)
fim = time()
t_exec = fim - inicio

print('merge_sort ordena {} números em {} segundos'.format(num, t_exec))
