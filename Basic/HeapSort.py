def sift(li, low, high):
    """
    :param li: list
    :param low: the position of root in the heap
    :param high: the position of the last element in the heap
    """
    i = low # index, as pointer1, point to root node
    j = 2 * i + 1 # the left node of i
    tmp = li[low] # store root value
    
    while j <= high:
        # if the right node exist, and greater than the left one
        if (j + 1 <= high) and (li[j + 1] > li[j]):
             j = j + 1 # then j point to the right node
        # if not, j still point to the left ndoe
        
        # compare a son node to its father node(root)
        if li[j] > tmp: # the son node greater than the fathter node
            li[i] = li[j] # move the son node to the father node
            i = j # dive into the next level
            j = 2 * i + 1
        else: # the father node greater than the son node
            li[i] = tmp # put the father node to the i position
            break
    else: # j > high
        li[i] = tmp # put tmp to the left node