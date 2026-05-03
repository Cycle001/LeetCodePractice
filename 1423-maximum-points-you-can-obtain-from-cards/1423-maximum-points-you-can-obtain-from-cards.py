class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        head = cardPoints[:k]
        tail = cardPoints[-1:-k-1:-1]
        tail = tail[::-1]
        canGet = tail + head
        ans = 0
        s = 0
        for right, x in enumerate(canGet):
            s += x
            if right < k-1:
                continue
            ans = max(ans, s)
            s -= canGet[right-k+1]
        return ans