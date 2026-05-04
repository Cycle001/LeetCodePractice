class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # 成环数组: i_next = (i_now + step) % n
        n = len(code)
        ans = [0 for _ in code]
        if k == 0:
            return ans
        elif k < 0:
            k = -k
            s = sum(code[n-k:])
            for right, x in enumerate(code):
                # i = (right) % n
                ans[right] = s

                left = (n-k + right) % n
                s += x - code[left]
        elif k > 0:
            s = sum(code[n-k:])
            for right, x in enumerate(code):
                i = (n-k-1 + right) % n
                ans[i] = s

                left = (n-k + right) % n
                s += x - code[left]
        return ans