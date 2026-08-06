class Solution:
    def longestPalindrome(self, s: str) -> str:
        str=""
        n=len(s)

        for  ch in range(n):
            a=self.expand(s,ch,ch)
            b=self.expand(s,ch,ch+1)

            if len(a)>len(str):
                str=a
            if len(b)>len(str):
                str=b
        
        return str
    
    def expand(self,s,left,right):
        
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        
        return s[left+1:right]
