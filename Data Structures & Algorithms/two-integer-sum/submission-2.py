class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = dict()
        for i, number in enumerate (nums) :
            res = target - number
            if res in dico :
                return [dico[res], i]
            else :
                dico[number] = i