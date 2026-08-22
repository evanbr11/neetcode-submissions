class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for s in details:
            if int(s[11 : len(s) - 2]) > 60:
                res += 1
        return res