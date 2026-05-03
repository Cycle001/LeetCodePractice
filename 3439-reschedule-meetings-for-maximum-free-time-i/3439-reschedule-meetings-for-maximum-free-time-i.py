class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        free_time = []
        last_endTime = [0] + endTime
        this_startTime = startTime + [eventTime]
        for right, (this_start, last_end) in enumerate(zip(this_startTime, last_endTime)):
            free = this_start - last_end
            free_time.append(free)
        
        sum_free_time = 0
        max_free_time = 0
        k = k + 1 # 不移动会议时 自带一个free time
        for right, time in enumerate(free_time):
            sum_free_time += time

            if right < k-1:
                continue
            max_free_time = max(max_free_time, sum_free_time)
            
            left = right -k+1
            sum_free_time -= free_time[left]
        print(free_time)
        print(right, max_free_time)
        return max_free_time