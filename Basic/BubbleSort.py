def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

def bubbleSort(list):
    l = len(list)
    if list is None or l < 2: return list
    # 0 ~ n-1
    # 0 ~ n-2
    # 0 ~ end--
    # 0 ~ 1
    for end in range(l-1, 0, -1): # 範圍從長到短
        for i in range(end): # i 跟 i+1 去比
            if list[i] > list[i+1]:
                swap(list, i, i+1)
    return list