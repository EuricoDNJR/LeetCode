class Solution:
    def shuffle(self, nums: list, n: int) -> list:
        ans_1 = nums[:n]
        ans_2 = nums[n:]
        ans = []
        for i in range(n):
            ans.append(ans_1[i])
            ans.append(ans_2[i])
        return ans


print(Solution().shuffle([2,5,1,3,4,7], 3))
