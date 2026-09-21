class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = dict()
        for i, num in enumerate (nums) :
            res = target - num
            if res in dico :
                return [dico[res], i]
            else :
                dico[num] = i