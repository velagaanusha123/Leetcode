class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = -1
        ch = '-1'
        arr = list(s)
        freq = {}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] = 1
        for i,count in freq.items():
            if(count==1):
                ch = i
                break
        if(ch!='-1'):
            index = s.index(ch) 
        return index
        