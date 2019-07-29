# Funções e bibliotecas necessárias
from random import randint
from bubble import bubbleSort
from insertion import insertionSort
from merge import mergeSort
from quick import quickSort
from quick import partition
from selection import selectionSort
from shell import shellSort
import timeit



array = []
while True:
    print("PROJETO 3 - ALGORITMOS DE ORDENAÇÃO\n")
    print("1 - Gerar o array randomicamente\n2 - Ordenar pelo BubbleSort\n3- Ordenar pelo InsertionSort\n4 - Ordenar pelo MergeSort\n5 - Ordenar pelo QuickSort\n6 - Ordenar pelo SelectionSort\n7 - Ordenar pelo ShellSort\n8 - Sair") 
    op = int(input("Digite a opção: "))
    if op == 8:
        break
    elif op == 1:
        for i in range(20000):
            array.append(randint(1,5000))
        print("Array gerado com sucesso\n")

    elif op == 2:
        print("Você escolheu o algoritmo BubbleSort\n")
        array_bub = array.copy()
        inicio = timeit.default_timer()
        result_bub  = bubbleSort(array_bub)
        fim = timeit.default_timer()
        result = fim - inicio
        print("Tempo de execução: {:.8f} \n".format(result))

    elif op == 3:
        print("Você escolheu o algoritmo InsertionSort\n")
        array_inser = array.copy()
        inicio = timeit.default_timer()
        result_inser = insertionSort(array_inser)
        fim = timeit.default_timer()
        result = fim - inicio
        print("Tempo de execução: {:.8f} \n".format(result))

    elif op == 4:
        print("Você escolheu o algoritmo MergeSort\n")
        array_merg = array.copy()
        inicio = timeit.default_timer()
        result_merg = mergeSort(array_merg)
        fim = timeit.default_timer()
        result = fim - inicio
        print("Tempo de execução: {:.8f} \n".format(result))

    elif op == 5:
        print("Você escolheu o algoritmo QuickSort\n")
        array_quic = array.copy()
        n= len(array_quic)
        inicio = timeit.default_timer()
        result_quic = quickSort(array_quic, 0, n-1)
        fim = timeit.default_timer()
        result = fim - inicio
        print("Tempo de execução: {:.8f} \n".format(result))

    elif op == 6:
        print("Você escolheu o algoritmo SelectionSort\n")
        array_selec = array.copy()
        inicio = timeit.default_timer()
        result_selec = selectionSort(array_selec)
        fim = timeit.default_timer()
        result = fim - inicio
        print("Tempo de execução: {:.8f} \n".format(result))

    elif op == 7:
        print("Você escolheu o algoritmo ShellSort\n")
        array_shel = array.copy()
        inicio = timeit.default_timer()
        result_shel = shellSort(array_shel)
        fim = timeit.default_timer()
        result = fim - inicio
        print("Tempo de execução: {:.8f} \n".format(result))

    else:
        print("Opção Inválida\n")
