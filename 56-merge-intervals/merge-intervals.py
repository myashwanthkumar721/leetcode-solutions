class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
       
        intervals.sort()

        ans=[]

        for intervals in intervals:
            if not ans or ans[-1][1] < intervals [0]:
                ans.append(intervals)
            else:
                ans[-1][1]=max(ans[-1][1],intervals[1])
        
        return ans