class Solution:
    def isPalindrome(self, x: int) -> bool:
        nn = str(x)
        new_list = []
        for i in range(len(nn)):
            new_list.append(nn[i])

        new_list_after = new_list[::-1]

        for j in range(len(new_list)):
            if new_list[j] != new_list_after[j]:
                return False
        return True