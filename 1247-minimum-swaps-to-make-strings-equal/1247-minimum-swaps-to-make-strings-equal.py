class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy_count = 0
        yx_count = 0

        for chars1 ,chars2  in zip(s1,s2):
            if chars1 == "x" and chars2 == "y":
                xy_count += 1
            elif chars1 == "y" and chars2 == "x":
                yx_count += 1
        
        if (yx_count + xy_count) % 2 == 1:
            return -1
        
        swap = (xy_count // 2) + (yx_count //2 )

        if yx_count % 2 == 1:
            swap += 2
        
        return swap 

        