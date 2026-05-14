class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        all_string = set()
        string = ''
        for i_r, x in enumerate(s):
            string += x
            if i_r < k-1:
                continue

            all_string.add(string)
            
            string = string[1:]
        return len(all_string) == 2**k