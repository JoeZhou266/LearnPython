def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count
if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    print(nums)
    count = removeElement(nums, 2)
    print(nums[0:count])
