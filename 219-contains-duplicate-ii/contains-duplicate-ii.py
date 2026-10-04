class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        freq = {}
        for i,num in enumerate(nums):
            if num in freq and (i - freq[num] <= k):
                return True
            freq[num] = i
        return False

        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]==nums[j] and abs(i - j) <= k):
        #             return True
        # return False
        