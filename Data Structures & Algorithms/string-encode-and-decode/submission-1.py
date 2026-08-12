class Solution:

    def __init__(self) -> None:
        self.lengths = [0]

    def encode(self, strs: List[str]) -> str:
        i = 1
        for s in strs:
            self.lengths.append(self.lengths[i - 1] + len(s))
            i += 1
        self.lengths[-1] += 1
        return ''.join(strs)

    def decode(self, s: str) -> List[str]:
        decode = []
        for i in range(len(self.lengths) - 1):
            decode.append(s[self.lengths[i]:self.lengths[i + 1]])
        return decode
