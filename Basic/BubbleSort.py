def bubble_sort(li):
    for i in range(len(li) - 1): # i round
        exchange = False
        for j in range(len(li) - i - 1): # unsorted list
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True

        if not exchange:
            return

l = [4, 23, 8, 42, 15, 16]
bubble_sort(li=l)
print(l)
