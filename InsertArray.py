
def insert(nums, position, value):
    assert position <= len(nums) and position != 0, "Position must be small than nums length"
    for i in range(len(nums) - 1, position - 1, -1):
        nums[i] = nums[i-1]
    nums[position - 1] = value
    return nums


if __name__ == '__main__':
    pyList = [-4,-1,0,3,10,0,0,0,0,99]
    nums = insert(pyList, 5, 100)
    print(nums)