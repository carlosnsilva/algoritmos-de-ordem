def selectionSort(arr):
    
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                aux = arr[j]
                arr[j] = arr[i]
                arr[i] = aux

    return arr
