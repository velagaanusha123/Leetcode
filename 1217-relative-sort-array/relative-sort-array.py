class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = []
        narr = []
        for i in range(len(arr2)):
            num = arr2[i]
            for j in range(len(arr1)):
                if(num==arr1[j]):
                    arr.append(num)
                    arr1[j] = -1
        for i in range(len(arr1)):
            if(arr1[i]!=-1):
                narr.append(arr1[i])
        narr.sort()
        return arr+narr
        
       
 
        