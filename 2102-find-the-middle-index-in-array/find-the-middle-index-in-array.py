class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        if(len(nums)==1):
            return 0
        elif(len(nums)==2):
            if(nums[1]==0):
                return 0
            elif(nums[0]==0):
                return 1
            else:
                return -1
        else:
            for i in range(len(nums)):
                suml = 0
                sumr = 0
                mi = i
                for j in range(0,mi,1):
                    suml += nums[j]
                for z in range(mi+1,len(nums),1):
                    sumr += nums[z]
                if(suml==sumr):
                    return mi
        return -1

        