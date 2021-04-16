def linearSearch(array, element):
    """
    :param array:
    :param element:
    :return: index in array, or -1 if not found
    """
    assert index >= 0, "index must be greater or equal zero"
    assert isinstance(array, list), "array must be list"

    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1


def linearPositionSearch(array, index, element):
    """
    :param array:
    :param index:
    :param element:
    :return: True if found element in index of array, or False if not found
    """
    assert index >= 0, "index must be greater or equal zero"
    assert isinstance(array, list), "array must be list"

    if array[index] == element:
        return True
    else:
        return False


if __name__ == '__main__':
    nums = [0,1,2,2,3,5,4,6]
    print(nums)
    index = linearSearch(nums, 2)
    print(index)
    index = linearSearch(nums, 7)
    print(index)
    index = linearSearch(nums, 0)
    print(index)
    index = linearSearch(nums, 6)
    print(index)

