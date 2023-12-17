import random
import copy
from SelectSort import selectSort
from BubbleSort import bubbleSort
from InsertSort import insertSort

def sameList(list1, list2):
    return list1 == list2

def random_list(length, max_val):
    return [random.randint(0, max_val) for _ in range(length)]

def validator(times):
    print("Start Testing")
    N = 100
    V = 1000
    for _ in range(times):
        n = random.randint(0, N)
        origin_list = random_list(length=n, max_val=V)
        list1 = copy.deepcopy(origin_list)
        list2 = copy.deepcopy(origin_list)
        list3 = copy.deepcopy(origin_list)
        selectSort(list1)
        bubbleSort(list2)
        insertSort(list3)
        if not (sameList(list1, list2) and sameList(list2, list3)):
            print("Different Result")
    print("Pass")

if __name__ == "__main__":
    validator(times=5000)