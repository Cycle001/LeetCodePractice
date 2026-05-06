from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        character1 = set(s1)
        count1 = Counter(s1)
        character2 = set()
        count2 = Counter()
        ans = False
        for i, c in enumerate(s2):
            character2.add(c)
            count2[c] += 1
            if i < k-1:
                continue

            if character1 == character2:
                flag = True
                for cha, cnt in count1.items():
                    if cnt != count2[cha]:
                        ans = False
                        flag = False
                        break
                if flag:
                    ans = True
            
            if ans == True:
                break
            left_cha = s2[i-k+1]
            count2[left_cha] -= 1
            if count2[left_cha] < 1:
                character2.remove(left_cha)
        return bool(ans)