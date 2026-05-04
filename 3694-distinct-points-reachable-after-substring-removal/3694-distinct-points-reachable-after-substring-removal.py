class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        def _move_one_step(coordinate, step, inverse=False):
            one = -1 if inverse else 1
            if step == 'U':
                coordinate[1] += one
            elif step == 'D':
                coordinate[1] -= one
            elif step == 'L':
                coordinate[0] -= one
            elif step == 'R':
                coordinate[0] += one
            return coordinate

        # 可到达的 不同 最终坐标的数量 == 移除子字符串 可到达的坐标的数量
        remove_final_coo = [0, 0]
        distinct_final_coo = set()
        for right, x in enumerate(s):
            remove_final_coo = _move_one_step(remove_final_coo, x)
            if right < k-1:
                continue

            distinct_final_coo.add(tuple(remove_final_coo))

            x_ = s[right-k+1]
            remove_final_coo = _move_one_step(remove_final_coo, x_, inverse=True)
        return len(distinct_final_coo)