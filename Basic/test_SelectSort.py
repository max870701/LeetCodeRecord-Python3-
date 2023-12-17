from SelectSort import selectSort

def test_selectSort():
    # Test case 1: Empty list
    input_list = []
    expected_output = []
    assert selectSort(input_list) == expected_output

    # Test case 2: List with one element
    input_list = [5]
    expected_output = [5]
    assert selectSort(input_list) == expected_output

    # Test case 3: List with duplicate elements
    input_list = [3, 1, 2, 1, 4, 2]
    expected_output = [1, 1, 2, 2, 3, 4]
    assert selectSort(input_list) == expected_output

    # Test case 4: List with already sorted elements
    input_list = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]
    assert selectSort(input_list) == expected_output

    # Test case 5: List with reverse sorted elements
    input_list = [5, 4, 3, 2, 1]
    expected_output = [1, 2, 3, 4, 5]
    assert selectSort(input_list) == expected_output

    # Test case 6: List with negative numbers
    input_list = [-5, -2, -3, -1, -4]
    expected_output = [-5, -4, -3, -2, -1]
    assert selectSort(input_list) == expected_output

    print("All test cases pass")

test_selectSort()