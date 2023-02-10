class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = [*jewels]
        stones = [*stones]
        acc = 0
        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    stone = '_'
                    acc += 1
        return acc

print(Solution().numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))