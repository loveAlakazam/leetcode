class Solution:
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        answer=[]
        for i in range(rowIndex+1):#i=0,1,...,rowIndex
            answer.append([])
            for j in range(i+1):#j=0,1,...,i
                if i==j or j==0:
                    answer[i].append(1)
                else:
                    answer[i].append(answer[i-1][j-1]+answer[i-1][j])
        
        return answer[rowIndex]
