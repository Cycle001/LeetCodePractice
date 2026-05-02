class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * len(nums)
        s = 0
        for right, x in enumerate(nums):
            s += x
            if right < 2*k:
                continue
            ans[right-k] = int(s / (2*k+1))
            s -= nums[right-2*k]
        return ans