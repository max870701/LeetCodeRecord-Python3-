def partition(array, l, r):
    pivot = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[r], array[i+1] = array[i+1], array[r]

    return i+1

def quick_sort(array, l, r):
    if l < r:
        pivot_index = partition(array, 0, len(array)-1)
        partition(array, 0, pivot_index-1)
        partition(array, pivot_index+1, len(array)-1)


if __name__ == "__main__":
    a = [1, 4, 5, 2, 8, 7, 9, 3, 6]
    quick_sort(a, 0, len(a)-1)
    print(a)