def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp: # From right side, search for nums less than tmp
            right -= 1  # the right pointer move 1 step to left
        li[left] = li[right] # Assign the right side value to left side position
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left] # Assign the left side value to right side position
    li[left] = tmp
    return left

def quick_sort(data, left, right):
    if left < right:
        mid  = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)

l = [7, 5, 4, 6, 3, 8, 2, 9, 1]
quick_sort(l, 0 , len(l)-1)
print(l)