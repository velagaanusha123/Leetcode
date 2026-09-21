class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        arr = []
        arr1 = []
        for i in range(len(nums)):
            if(i%2==0 and nums[i]%2!=0): 
                arr.append(i)
            elif(i%2!=0 and nums[i]%2==0):
                arr1.append(i)
        for i in range(len(arr)):
            temp = nums[arr[i]]
            nums[arr[i]] = nums[arr1[i]]
            nums[arr1[i]] = temp 
        return nums




        