class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max = 0

        ordre = set(nums)
        for elem in ordre:
            if (elem-1) not in ordre :
                i=1
                while (elem+i) in ordre:
                    i+=1
                if i>max:
                    max=i
        return max