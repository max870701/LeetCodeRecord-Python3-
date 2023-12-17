def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

def selectSort(list):
    l = len(list)
    if list is None or l < 2:return list
    # 0 ~ n-1
    # 1 ~ n-1
    for i in range(l-1): # 設置當前 index 為最小值的index
        minIndex = i
        for j in range(i+1, l): # j 從 i+1 開始，到 l-1 最後一項結束
            if (list[j] < list[minIndex]):
                minIndex = j # 更新最小值 index
        swap(list, i, minIndex)
    return list