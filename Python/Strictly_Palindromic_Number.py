class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        result = n
        for base in range(2, n-1):
            res = []
            while result != 0:
                res.append(str(result % base)) 
                result//=base
            if res != res[::-1]:
                return False
            result = n
        return True


# test = ['1', '0', '0']
# test.append(str(1 % 2))
# print(test[::-1])
print(Solution().isStrictlyPalindromic(n = 9))

