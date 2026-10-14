class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = dict()
        for indice, value in enumerate(nums):
            diff = target - value
            if diff in dico:
                return [dico[diff], indice]
            dico[value] = indice
                