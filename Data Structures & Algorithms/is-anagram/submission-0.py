class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettermap1 = {}
        lettermap2 = {}
        for letter in s:
            lettermap1[letter] = lettermap1.get(letter, 0) + 1
        for letter in t:
            lettermap2[letter] = lettermap2.get(letter, 0) + 1
        if lettermap1 == lettermap2:
            return True
        else:
            return False