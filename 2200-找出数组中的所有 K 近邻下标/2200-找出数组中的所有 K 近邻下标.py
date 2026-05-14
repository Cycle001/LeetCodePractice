from collections import Counter
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        window = k + 1
        cnt = Counter()
        ans = []
        left_neighbour = []
        for i, n in enumerate(nums):
            cnt[n] += 1
            left_neighbour.append(i)
            if i < window-1: # 进入窗口前
                if i + 1 == len(nums): # 窗口未形成nums已结束
                    if cnt[key] > 0:
                        ans += left_neighbour
                        left_neighbour = []
                continue
            
            if cnt[key] > 0:
                ans += left_neighbour
            
            i_left = i - window+1
            n_left = nums[i_left]
            cnt[n_left] -= 1
            if left_neighbour:
                left_neighbour.pop(0)
        unique = []
        ans = [unique.append(x) for x in ans if x not in unique]
        return unique
