def insert_sort(li):
    for i in range(1, len(li)): # the index of hand card we pick (unsorted area)
        temp = li[i]
        # the maximum index of hand card we have (Right Side in sorted area)
        j = i - 1
        while li[j] > temp and j >= 0:
            li[j+1] = li[j] 
            j -= 1
        
        # if j < 0 OR
        # if li[j] < temp
        li[j+1] = temp
        print(li)

l = [7, 5, 4, 6, 3, 8, 2, 9, 1]
print(l)
insert_sort(l)
#print(l)