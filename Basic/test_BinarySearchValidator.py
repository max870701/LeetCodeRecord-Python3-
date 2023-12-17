from BinarySearch import numExist
import random

def numExistRight(list, num):
    for n in list:
        if n == num:
            return True
    return False

def random_list(length, max_val):
    return [random.randint(0, max_val) for _ in range(length)]

def validator(times):
    print("Start Testing")
    N = 100
    V = 1000
    for _ in range(times):
        n = random.randint(0, N)
        origin_list = random_list(length=n, max_val=V)
        sort_list = sorted(origin_list)
        num = random.randint(0, N)
        if numExistRight(sort_list, num) != numExist(sort_list, num):
            print("Different Result")
            print(sort_list)
    print("Pass")

if __name__ == "__main__":
    validator(times=50000)