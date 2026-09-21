class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        height = sorted(heights)
        for i in range(len(heights)):
            if(heights[i] != height[i]):
                count+=1
        return count
        