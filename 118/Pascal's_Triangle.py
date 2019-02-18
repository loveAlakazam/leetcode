class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        answer=[]
        for i in range(1, numRows+1):#i=1,2,3,..,numRows
            answer.append([])
            for j in range(1, i+1):#j=1,2,...,i
                if j==1 or j==i:
                    answer[(i-1)].append(1)
                else:#j!=1 and j!=i
                    answer[(i-1)].append(answer[(i-1)-1][(j-1)-1]+answer[(i-1)-1][(j-1)])
        return answer
