def bubbleSort(arr):
    t  = True
    while t:
        t = False
        for i in range(1 , len(arr)):
            if arr[i] < arr[i -1]:
                aux = arr[i]
                arr[i] = arr[i-1]
                arr[i -1] = aux
                t = True
    return arr


    
