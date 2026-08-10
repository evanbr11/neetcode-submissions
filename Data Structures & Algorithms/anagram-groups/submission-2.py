class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = defaultdict(list)
        for s in strs:
            temp = "".join(sorted(s))
            sorted_words[temp].append(s)
        return list(sorted_words.values())
