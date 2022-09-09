def bubble_sort(li):
    for i in range(len(li) - 1): # i round
        exchange = False
        for j in range(len(li) - i - 1): # unsorted list
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True

        if not exchange:
            return

l = [7, 5, 4, 6, 3, 8, 2, 9, 1]
bubble_sort(li=l)
print(l)