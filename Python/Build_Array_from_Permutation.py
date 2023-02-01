class Solution:
    def buildArray(self, nums: list) -> list:
        output = []
        for _, v in enumerate(nums):
            output.append(nums[v])
        return output

#test
nums = [0,2,1,5,3,4]
print(Solution().buildArray(nums))