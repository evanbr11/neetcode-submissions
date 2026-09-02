class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur = -1
        for i in range(len(arr) - 1, -1, -1):
            new_cur = max(cur, arr[i])
            arr[i] = cur
            cur = new_cur
        return arr