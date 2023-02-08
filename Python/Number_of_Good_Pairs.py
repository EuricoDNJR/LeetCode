class Solution:
    def numIdenticalPairs(self, nums: list) -> int:
        good = 0
        for i, v in enumerate(nums):
            for j in range(i, len(nums)):
                if v == nums[j] and i < j:
                    good += 1
        return good

print(Solution().numIdenticalPairs([1,2,3,1,1,3]))
print(Solution().numIdenticalPairs([1,1,1,1]))
print(Solution().numIdenticalPairs([1,2,3]))