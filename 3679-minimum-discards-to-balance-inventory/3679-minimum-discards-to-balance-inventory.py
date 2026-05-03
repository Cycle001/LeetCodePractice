from collections import Counter
from collections import deque
class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        cnt = Counter()
        dis = dq = deque([])
        ans = 0
        for right, x in enumerate(arrivals):
            cnt[x] += 1
            
            if cnt[x] > m:
                ans += 1
                cnt[x] -= 1
                # 由于已经丢弃，不能在离开窗口时修改 cnt
                dis.append(right)
            
            if right < w-1:
                continue
            left = right-w+1
            if len(dis) > 0 and left == dis[0]: # 离开窗口时不修改 cnt
                dis.popleft()
            else:
                cnt[arrivals[left]] -= 1
        return ans