class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        sub = []
        s = 0
        ans = 0
        for right, x in enumerate(nums):
            sub[:0] = [x]
            s += x
            if right < k-1:
                continue
            if len(set(sub)) >= m:
                ans = max(s,ans)
            sub.pop(-1)
            s -= nums[right - k+1]
        return ans