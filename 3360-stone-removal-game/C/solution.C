bool canAliceWin(int n) {
    int curr = 10;
    bool a = true;
    while (curr>0){
        if (curr<=n){
            n-=curr;
            curr--;
            a = !a;
        }
        else return !a;
    }
    return !a;
}