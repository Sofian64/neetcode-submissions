class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for elem in nums:
            if elem in res:
                return True
            res.add(elem)
        return False