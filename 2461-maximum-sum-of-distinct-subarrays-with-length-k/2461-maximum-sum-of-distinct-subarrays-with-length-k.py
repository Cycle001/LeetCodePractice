from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        s = 0
        cnt = Counter()
        for right, x in enumerate(nums):
            s += x
            cnt[x] += 1
            
            if right < k-1:
                continue
            if len(cnt) == k:
                ans = max(ans,s)
            
            x_ = nums[right-k+1]
            s -= x_
            cnt[x_] -= 1
            if cnt[x_] < 1:
                cnt.pop(x_)
        return ans