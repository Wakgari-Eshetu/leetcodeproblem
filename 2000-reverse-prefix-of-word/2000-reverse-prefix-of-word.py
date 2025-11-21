class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        if ch in word:
            idx = word.index(ch)
            w1 = ''.join(reversed(word[:idx+1]))
            w2 = word[idx+1:]
            return w1+w2
        
        return word




        