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

    li[left] = tmp    
 






l = [7, 5, 4, 6, 3, 8, 2, 9, 1]