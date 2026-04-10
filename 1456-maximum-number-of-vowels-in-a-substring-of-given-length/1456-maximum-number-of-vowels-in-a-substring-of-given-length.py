class Solution:
    def countOfVowels(self, vowel, s):
        count = 0
        for i in range(len(s)):
            if s[i] in vowel:
                count += 1
        return count
    
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ['a','e','i','o','u']
        cur_vowels = self.countOfVowels(vowel, s[0:k])
        max_vowels = cur_vowels
        for i in range(1,len(s)-k+1):
            if s[i-1] in vowel:
                cur_vowels = cur_vowels - 1
            if s[i+k-1] in vowel:
                cur_vowels = cur_vowels + 1
            # cur_vowels = self.countOfVowels(vowel, s[i:i+k])
            if max_vowels < cur_vowels:
                max_vowels = cur_vowels
            if max_vowels == k:
                break
        return max_vowels
