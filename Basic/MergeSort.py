def merge(li, low, mid, high):
    i = low
    j = mid + 1
    tmp_list = []
    # To ensure there are two nubmers on both sides
    while i <= mid and j <= high:
        if li[i] < li[j]:
            tmp_list.append(li[i])
            i += 1
        else: # li[j] < li[i]
            tmp_list.append(li[j])
            j += 1
    # There is not any number in i or j
    while i <= mid:
        tmp_list.append(li[i])
        i += 1
    while j <= high:
        tmp_list.append(li[j])
        j += 1
    li[low:high+1] = tmp_list


def merge_sort(li, low, high):
    if low < high: # at least two elements
        mid = (low + high) // 2 
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)  