# 有序list中找num是否存在
def numExist(list, num):
    left, right = 0, len(list)-1
    while (left <= right):
        # mid = (left + right) // 2
        # 防止溢出， >>位運算
        mid = left + ((right - left) >> 1)
        if list[mid] == num:
            return True
        elif list[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return False

# 有序數組中找 >= num 的最左位置
def findLeftNumIndex(list, num):
    left, right = 0, len(list) - 1
    ans = -1
    while left<= right:
        mid = left + ((right - left) >> 1)
        if list[mid] >= num:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

# 有序數組中找 <= num 的最右位置
def findRightNumIndex(list, num):
    left, right = 0, len(list) - 1
    ans = -1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if list[mid] <= num:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans

# 尋找峰值問題
def findPeakElement(list):
    n = len(list)
    if n == 1:
        return 0
    # If index 0 is a peak
    if list[0] > list[1]:
        return 0
    # If index n-1 is a peak
    if list[n-1] > list[n-2]:
        return n-1
    # If both index 0, n-1 are not peak
    left, right = 1, n-2
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] < list[mid-1]:
            right = mid - 1
        elif list[mid] < list[mid+1]:
            left = mid + 1
        else:
            ans = mid
            break
    return ans