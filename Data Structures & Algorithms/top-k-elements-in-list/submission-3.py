class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for key, v in count.items():
            buckets[v].append(key)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res