class Solution:
    def numberOfSteps(self, num: int) -> int:
        acc = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            acc += 1

        return acc
    
print(Solution().numberOfSteps(8))
