
class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result

class Solution2(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pyList = [-4,-1,0,3,10]
    solution = Solution()
    print(solution.sortedSquares(pyList))
    solution2 = Solution2()
    print(solution2.sortedSquares(pyList))