int scoreOfParentheses(char* s) {
    int res = 0;
    int depth =0;
    int n = strlen(s);
    
    for (int i=0;i<n;i++)
    {
        if (s[i]=='(')
        {
            depth++;
        }
        else{
            depth--;
            if (s[i-1]=='('){
                res+= 1<<depth;
            }
        }
    }
    return res;
}