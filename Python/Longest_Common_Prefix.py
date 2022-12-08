class Solution:
    def myFunc(self, e):
        return len(e)
        
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=self.myFunc)
    
        
        for string in strs[1:]:
            for i, char in enumerate(strs[0]):
                if char != string[i]:
                    strs[0] = strs[0][0:i]
                    break
        
        return strs[0]