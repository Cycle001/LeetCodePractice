from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        character_p = set(p)
        count_p = Counter(p)
        character_s = set()
        count_s = Counter()
        ans = []
        for right, cha in enumerate(s):
            character_s.add(cha)
            count_s[cha] += 1
            if right < k-1:
                continue
            
            left = right -k+1
            if character_p == character_s:
                flag = True
                for cha, cnt in count_p.items():
                    if cnt != count_s[cha]:
                        flag = False
                if flag:
                    ans.append(left)
            
            cha_left = s[left]
            count_s[cha_left] -= 1
            if count_s[cha_left] < 1:
                character_s.remove(cha_left)
        return ans