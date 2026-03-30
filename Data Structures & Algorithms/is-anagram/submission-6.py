class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            char = s[i]
            if char in countS:
                countS[char] +=1
            else:
                countS[char] = 1

        for j in range(len(t)):
            char = t[j]
            if char in countT:
                countT[char] +=1
            else:
                countT[char] = 1

        if countS == countT:
            return True
        else:
            return False