char* removeOuterParentheses(char* s) {
    int n = strlen(s);
    char* res = (char*)malloc(sizeof(char)*(n+1));
    int depth=0;
    int idx = 0;
    for (int i=0;i<n;i++){
        if (s[i]==')') depth--;
        if (depth>0){
            res[idx++]=s[i];
        }
        if(s[i]=='(')depth++;
    }
    res[idx]='\0';
    return res;
}