class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        products = sorted(products)
        for i in range(len(searchWord)):
            val = searchWord[:i+1]
            result = []
            for pro in products:
                if pro.startswith(val):
                    result.append(pro)
            ans.append(result[:3])
        return ans 
