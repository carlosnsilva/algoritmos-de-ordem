def insertionSort(arr):
    cont = 0
    for i in range(1 , len(arr)):
        atual = arr[i]
        pos = i -1
        while pos >= 0 and atual < arr[pos]:
            arr[pos+1] = arr[pos]
            pos = pos - 1
            cont = cont + 1

        arr[pos+1] = atual

    return arr


