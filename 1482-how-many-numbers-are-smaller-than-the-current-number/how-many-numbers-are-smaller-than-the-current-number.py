class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            count = 0
            num = nums[i]
            for j in range(len(nums)):
                if(num>nums[j]):
                    count+=1
            arr.append(count)
        return arr
        