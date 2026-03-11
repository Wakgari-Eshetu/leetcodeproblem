class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff_array = [0] * (n + 1)
        for start_idx, end_idx, direction in shifts:
            if direction == 0:
                direction = -1
            diff_array[start_idx] += direction
            diff_array[end_idx + 1] -= direction
    
        for i in range(1, n + 1):
            diff_array[i] += diff_array[i - 1]
      
       
        result_chars = []
        for i in range(n):
            original_pos = ord(s[i]) - ord('a')
            new_pos = (original_pos + diff_array[i] + 26) % 26
            result_chars.append(chr(ord('a') + new_pos))
        return ''.join(result_chars)
