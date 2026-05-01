class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = set()
        left_pre = right_pre = 0
        for pre in s:
            if pre == '(':
                left_pre += 1
            elif pre == ')':
                if left_pre == 0:
                    right_pre += 1
                else:
                    left_pre -= 1
        def dfs(index , path , left_pre , right_pre , count):
            if index == len(s):
                if left_pre == 0 and right_pre == 0 and count == 0:
                    result.add(path)
                return 
            
            char = s[index]

            if char == '(' and left_pre > 0:
                dfs(index+1 , path , left_pre - 1 , right_pre , count)
            elif char == ')' and right_pre > 0:
                dfs(index+1 , path , left_pre , right_pre - 1 , count )

            
            if char not in '()':
                dfs(index + 1, path + char, left_pre, right_pre, count)
            elif char == '(':
                dfs(index + 1, path + char, left_pre, right_pre, count + 1)
            elif char == ')' and count > 0:
                dfs(index + 1, path + char, left_pre, right_pre, count - 1)

        dfs(0, "", left_pre, right_pre, 0)
        return list(result)




        