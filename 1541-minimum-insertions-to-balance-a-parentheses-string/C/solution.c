int minInsertions(char* s) {
    int left = 0;
    int right = 0;
    int n = strlen(s);
    for (int i=0;i<n;i++){
        if (s[i]=='('){
            if (right%2==1){
                left++;
                right--;
            }
            right+=2;
        }
        else{
            right--;
            if (right<0){
                left++;
                right = 1;
            }
        }
    }
    return left + right;
}