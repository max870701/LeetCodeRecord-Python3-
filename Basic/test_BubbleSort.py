from BubbleSort import bubbleSort

def test_bubbleSort():
    # Test case 1: Empty list
    assert bubbleSort([]) == []

    # Test case 2: List with one element
    assert bubbleSort([5]) == [5]

    # Test case 3: List with two elements in ascending order
    assert bubbleSort([2, 5]) == [2, 5]

    # Test case 4: List with two elements in descending order
    assert bubbleSort([5, 2]) == [2, 5]

    # Test case 5: List with multiple elements in random order
    assert bubbleSort([4, 2, 7, 1, 5]) == [1, 2, 4, 5, 7]

    # Test case 6: List with duplicate elements
    assert bubbleSort([3, 1, 2, 1, 4, 2]) == [1, 1, 2, 2, 3, 4]

    # Test case 7: List with negative numbers
    assert bubbleSort([-5, -2, -7, -1, -3]) == [-7, -5, -3, -2, -1]

    # Test case 8: List with already sorted elements
    assert bubbleSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    print("All test cases passed")

test_bubbleSort()