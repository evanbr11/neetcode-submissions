class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            return 1
        j = len(s)
        while s[j - 1] == " ":
            j -= 1
        i = j
        while s[i - 1] != " ":
            i -= 1
        return len(s[i : j])
            