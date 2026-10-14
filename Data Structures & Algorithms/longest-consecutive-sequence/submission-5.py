class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max, temp = 1, 1

        if len(nums)==0:
            return 0

        ordre = set(nums)
        for elem in ordre:
            if (elem-1) in ordre :
                continue
            else:
                i=1
                while (elem+i) in ordre:
                    temp+=1
                    i+=1
                if temp>max:
                    max=temp
                temp = 1
        return max