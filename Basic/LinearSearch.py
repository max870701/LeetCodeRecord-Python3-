def linear_search(data_set, value):
    for i in range(len(data_set)):
        if data_set[i] == value:
            return i
    return None