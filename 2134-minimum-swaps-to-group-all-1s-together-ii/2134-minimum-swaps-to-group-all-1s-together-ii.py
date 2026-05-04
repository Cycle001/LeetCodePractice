from collections import Counter
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window = Counter()
        n = len(nums)
        for num in nums:
            window[num] += 1
        k = window[1]
        # 特殊情况
        if k == 0 or k == n:
            return 0

        # 环: 窗口先覆盖最后 k-1 个元素, 再滑动窗口
        max_ = 0
        sum_ = sum(nums[n-k+1:]) # n- (k-1) .. n- 1
        for right, num in enumerate(nums):
            sum_ += num
            
            max_ = max(max_, sum_)

            if right < k-1:
                left = n-k+1 + right
                sum_ -= nums[left]
            else:
                left = right - k+1
                sum_ -= nums[left]
        return k - max_