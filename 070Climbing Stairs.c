int climbStairs(int n) {
        //n개 만큼 동적할당
        int * arr = (int *)malloc(sizeof(int)*(n+1));
        arr[0]=1, arr[1]=1;
        if(n>=2){
            int i;
            for(i=2;i<=n;i++)
                arr[i]=arr[i-1]+arr[i-2];
        }
        return arr[n];
}
