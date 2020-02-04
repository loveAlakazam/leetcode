import sys

def solution(g,s):
    g=sorted(g)
    s=sorted(s)
    leng=len(g)
    lens=len(s)
    cnt=0
    i,j=0,0
    while i< leng and j<lens:
        print('g[i]: {}, s[j]: {}'.format(g[i], s[j]))
        if g[i]<=s[j]:
            cnt+=1
            i+=1
            j+=1
        else:#g[i]>s[j]
            j+=1
    return cnt
                
def main():
    T=int(sys.stdin.readline())
    for _ in range(T):
        g=list(map(int, sys.stdin.readline().split()))
        s=list(map(int, sys.stdin.readline().split()))
        result=solution(g,s)
        print(result,'\n')

if __name__=='__main__':
    main()
