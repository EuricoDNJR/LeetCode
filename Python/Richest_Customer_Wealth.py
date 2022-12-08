class Solution:
    def maximumWealth(self, accounts):
        amount = 0
        m = len(accounts)

        richest_value = 0
        for a in range(m):
            for b in range(len(accounts[a])):
                amount += accounts[a][b]
            if a == 0:
                richest_value = amount
            elif amount > richest_value:
                richest_value = amount
            amount = 0
        return richest_value