int romanToInt(char* s) {
    //I: 1 V : 5, X: 10, L:50, C:100, D:500, M:1000
    int l = strlen(s);
    int n[l];
    int r[l];
    int sum=0;
    int i, index=0;
    for(i=0;i<l;i++) //ÃÊ±âÈ­
        r[i]=0;
    
    for(i=0;i<l; i++ ){
        switch(s[i]){
            case 'I': n[i]=1;break;
            case 'V': n[i]=5;break;
            case 'X': n[i]=10; break;
            case 'L': n[i]=50; break;
            case 'C': n[i]=100; break;
            case 'D': n[i]=500; break;
            case 'M': n[i]=1000; break;
        }
    }
    
    for(i=0;i<l-1;i++){
        if(n[i]<n[i+1]){
          r[index++]= n[i+1]-n[i];
          i++;  
         } 
        else r[index++]=n[i];
    }
    
    if(l>=2){
        if(n[l-1]<=n[l-2])
            r[index]= n[l-1];

        for(i=0;i<l;i++)
            sum+=r[i];
    }
    
    else{// l<=1
        sum = n[0];
    } 
           
    return sum;
}
