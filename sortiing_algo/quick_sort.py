

def quickSort(arr, s, e):

    if (e - s + 1) <= 1:
        return arr

    pivot = arr[e]

    left = s

    for i in range (s,e):

        if arr[i] < pivot:
            temp = arr[left]
            arr[left] = arr[i]
            arr[i] = temp
            left += 1

    quickSort(arr, s, left - 1)
    quickSort(arr,left + 1, e)

    return arr