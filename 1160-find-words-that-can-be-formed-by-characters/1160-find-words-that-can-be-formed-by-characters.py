class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def check_the_word(word,chars)->bool:
            i = 0
            while i < len(word):
                if word[i] not in chars:
                    return False 
                    
                i+=1
            return True   

        ans  = 0  
        for word in words:
            flag = check_the_word(word,chars)
            if flag:
                ans += len(word)
        
        return ans 

        