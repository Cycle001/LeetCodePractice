class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # all_string = ['']
        # for _ in range(k):
        #     new = []
        #     for x in all_string:
        #         new.append(x + '0')
        #         new.append(x + '1')
        #     all_string = new
        # # print(all_string)
        all_string = set()
        string = ''
        for i_r, x in enumerate(s):
            string += x
            if i_r < k-1:
                continue

            all_string.add(string)
            
            string = string[1:]
        return len(all_string) == 2**k