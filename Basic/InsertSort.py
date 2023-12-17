def insertSort(list):
    l = len(list)
    if l is None or l < 2: return list
    # 0 ~ 0, 1
    # 0 ~ 1, 2
    # ...
    # 0 ~ n-2, n-1
    for i in range(1, l):
        for j in range(i-1, -1, -1):
            if list[j+1] < list[j]:
                swap(list, j, j+1)
    return list

def swap(list, i, j):
    list[i], list[j] = list[j], list[i]