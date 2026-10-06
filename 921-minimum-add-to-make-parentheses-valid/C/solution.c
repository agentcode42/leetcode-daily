int minAddToMakeValid(char* s) {
    int count=0;
    int res = 0;
    int n = strlen(s);
    for (int i=0;i<n;i++){
        if (s[i]=='(') count++;
        else{
            count--;
            if (count<0){
                res++;
                count++;
            }
        }
    }
    return res+count;
}