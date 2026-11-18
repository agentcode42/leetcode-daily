int minChanges(char* s) {
    int n = strlen(s);
    int result =0;
    for(int i=0;i<n;i+=2){
        if (s[i]!=s[i+1]){
            result++;
        }
    }
    return result;
}