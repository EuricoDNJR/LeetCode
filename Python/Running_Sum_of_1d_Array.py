class Solution:
    def runningSum(self, nums: list) -> list:
        ans = []
        acc = 0
        for _, v in enumerate(nums):
            acc += v
            ans.append(acc)
        return ans

print(Solution().runningSum([1,2,3,4]))
print(Solution().runningSum([1,1,1,1,1]))
print(Solution().runningSum([3,1,2,10,1]))