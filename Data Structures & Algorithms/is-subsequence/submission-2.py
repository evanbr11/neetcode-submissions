class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        if s == t:
            return True

        i = j = 0

        while i < len(s):
            if j >= len(t):
                    return False
            elif s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        return True