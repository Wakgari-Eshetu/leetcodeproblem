class Solution:
    def bitwiseComplement(self, n: int) -> int:
        string = bin(n)[2:]
        string = list(string)
        for i in range(len(string)):
            if string[i] == '0':
                string[i] = '1'
            else:
                string[i] = '0'
        string = ''.join(string)
        return int(string, 2)

        