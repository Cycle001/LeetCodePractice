class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = -10**4
        average = 0
        for right, x in enumerate(nums[k-1:],k-1):
            # if right < k-1:
            #     continue
            average = sum(nums[right-k+1:right+1]) / k
            ans = average if average > ans else ans
        return ans