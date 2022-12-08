class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                amount = nums[i] + nums[j]
                if(amount == target):
                    output.append(i)
                    output.append(j)
                    return output
                amount = 0

