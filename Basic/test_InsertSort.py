from InsertSort import insertSort

def test_insertSort():
    # Test case 1: Empty list
    arr = []
    insertSort(arr)
    assert arr == []

    # Test case 2: List with one element
    arr = [5]
    insertSort(arr)
    assert arr == [5]

    # Test case 3: List with multiple elements in ascending order
    arr = [1, 2, 3, 4, 5]
    insertSort(arr)
    assert arr == [1, 2, 3, 4, 5]

    # Test case 4: List with multiple elements in descending order
    arr = [5, 4, 3, 2, 1]
    insertSort(arr)
    assert arr == [1, 2, 3, 4, 5]

    # Test case 5: List with multiple elements in random order
    arr = [3, 1, 4, 2, 5]
    insertSort(arr)
    assert arr == [1, 2, 3, 4, 5]

    print("All test cases pass")

test_insertSort()