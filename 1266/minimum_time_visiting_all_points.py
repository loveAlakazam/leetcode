class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points)<=1:
            return 0
        
        cnt=0
        for i in range(len(points)-1):
            start=points[i]
            end=points[i+1]
            
            dx=abs(end[0]-start[0])
            dy=abs(end[1]-start[1])
            
            #대각선이동: dy,dx중 작은값만큼 대각선으로 이동
            cross_shift=min(dy, dx)
            cnt+=cross_shift
            dx-=cross_shift
            dy-=cross_shift
            
            #나머지 이동
            if dx>0:
                cnt+=dx
            elif dy>0:
                cnt+=dy
        return cnt
