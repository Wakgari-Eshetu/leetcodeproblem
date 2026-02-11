class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic = { indices[i] :val  for i , val in enumerate(s)}
        return "".join(dic[i] for i in range(len(s)))