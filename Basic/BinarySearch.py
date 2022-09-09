def binary_search(li, val):
    left = 0
    right = len(li) - 1

    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        elif li[mid] < val:
            left = mid + 1
    else:
        return None

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(li=l, val=3))