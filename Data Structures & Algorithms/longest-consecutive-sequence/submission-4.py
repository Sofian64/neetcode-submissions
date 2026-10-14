class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        ordre = sorted(set(nums))
        max, temp = 1, 1
        for i in range (len(ordre)-1):
            if (ordre[i]+1) == ordre[i+1]:
                temp+=1
                if temp>max:
                    max=temp
            else:
                temp=1
        return max