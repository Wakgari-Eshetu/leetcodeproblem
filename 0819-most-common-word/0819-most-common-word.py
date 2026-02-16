class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count = Counter(re.findall(r"[a-z]+", paragraph.lower()))
        for char , value in count.most_common():
            if char not in banned:
                return char 

