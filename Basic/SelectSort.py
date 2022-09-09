def select_sort_simple(li):
    li_new = [] # it will double the memory
    for i in range(len(li)): # O(N)
        min_val = min(li) # O(N)
        li_new.append(min_val)
        li.remove(min_val) # O(N)
    return li_new

def select_sort(li):
    for i in range(len(li) - 1): # i round
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
        print(li)




li = [3, 2, 4, 1, 5, 6, 8, 7, 9]
print(li)
#print(select_sort_simple(li))
select_sort(li)