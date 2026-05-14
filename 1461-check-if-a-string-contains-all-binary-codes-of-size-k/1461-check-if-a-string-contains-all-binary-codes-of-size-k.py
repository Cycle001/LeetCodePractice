class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        MASK = (1 << k) - 1
        st = set()  # 更快的写法见另一份代码【Python3 列表】
        x = 0
        for i, ch in enumerate(s):
            # 把 ch 加到 x 的末尾：x 整体左移一位，然后或上 ch
            # &MASK 目的是去掉超出 k 的比特位
            x = (x << 1 & MASK) | int(ch)
            if i >= k - 1:
                st.add(x)
        return len(st) == 1 << k

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/check-if-a-string-contains-all-binary-codes-of-size-k/solutions/3902489/liang-chong-fang-fa-bao-li-wei-yun-suan-4wnph/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。