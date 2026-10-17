class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ord = set(nums)
        maxi = 0
        for elem in ord:
            if (elem - 1) in ord:
                continue
            else :
                temp = 1
                while (elem + temp) in ord:
                    temp+=1
                if temp > maxi:
                    maxi = temp
        return maxi