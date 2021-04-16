from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)

        for i in range(length - 2, -1, -1):
            if nums[i] == nums[i + 1]:
                for j in range(i + 1, length, 1):
                    nums[j - 1] = nums[j]
                length -= 1
        return length


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pyList = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(pyList)
    solution = Solution()
    length = Solution().removeDuplicates(pyList)
    print(pyList[0:length])
