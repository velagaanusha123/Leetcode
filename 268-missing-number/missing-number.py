class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        freq = {i:0 for i in range(0,len(nums)+1)}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] = 1
        for i,count in freq.items():
            if(count!=1):
                return i


        