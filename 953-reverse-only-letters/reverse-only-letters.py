class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = 0
        r = len(s)-1
        s = list(s)
        while(l <= r):
            if(s[l].isalpha()==True and s[r].isalpha()==True):
                ch = s[l]
                s[l] = s[r]
                s[r] = ch
                l+=1
                r-=1
            elif(s[l].isalpha()==False):
                l+=1
            elif(s[r].isalpha()==False):
                r-=1
        s = ''.join(s)
        return s




            


             
            
        