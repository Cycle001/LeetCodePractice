class Solution:
    def queryString(self, s: str, n: int) -> bool:
        num = 0
        for _ in range(1, n+1):
            num += 1
            string = f"{num:b}"
            if string not in s:
                return False
        return True