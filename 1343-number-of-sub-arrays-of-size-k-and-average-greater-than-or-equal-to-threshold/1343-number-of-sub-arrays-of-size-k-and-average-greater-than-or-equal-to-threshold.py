class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = 0
        ans = 0
        for right, x in enumerate(arr):
            s += x
            if right < k-1:
                continue
            if s / k >= threshold:
                ans += 1
            s -= arr[right-k+1]
        return ans
            