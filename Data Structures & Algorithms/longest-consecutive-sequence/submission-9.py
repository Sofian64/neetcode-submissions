class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ord = set(nums)
        maxi = 1 
        if len(ord) == 0:
            return 0
        for elem in ord:
            if (elem - 1) in ord:
                continue
            else :
                i = 1
                temp = 1
                while (elem + i) in ord:
                    temp+=1
                    i+=1
                if temp > maxi:
                    maxi = temp
        return maxi