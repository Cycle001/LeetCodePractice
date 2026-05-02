from collections import Counter
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cnt = 0
        max_color = 0
        for right, c in enumerate(blocks): 
            if c == 'B':
                cnt += 1
            if right < k-1:
                continue
            max_color = max(cnt,max_color)
            if blocks[right - k+1] == 'B':
                cnt -= 1
        return k - max_color