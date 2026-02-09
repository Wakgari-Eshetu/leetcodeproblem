class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common  = strs[0]
        common_len = len(common)

        for i in strs[1:]:
            while common!= i[0:common_len]:
                common_len -= 1
                if common_len == 0:
                    return ""
                common = common[0:common_len]

        return common 

        
