bool judgeCircle(char* moves) {
    int x=0, y=0;
    char direction;
    int movesLength = strlen(moves);
    int i;
    
    for(i=0; i<movesLength; i++ ){
        switch(moves[i]){
            case 'U':y++; break;
            case 'D':y--; break;
            case 'L':x--; break;
            case 'R':x++; break;
        }
    }
    if(x==0 && y==0) return true; //돌아옴..
    else return false;
}
