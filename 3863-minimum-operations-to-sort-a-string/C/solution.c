int minOperations(char* s) {
    char mins = s[0];
    char maxs = s[0];
    int n = strlen(s);
    bool sort = true;
    for (int i=1;i<n;i++){
        if (s[i]<s[i-1]) sort = false;
        if (s[i]<mins)mins=s[i];
        if (s[i]>maxs)maxs=s[i];
    }
    if (sort)return 0;
    if (n==2)return -1;
    if (s[0]==mins || s[n-1]==maxs)return 1;
    for (int i=1;i<n-1;i++){
        if (s[i]==mins || s[i]==maxs)return 2;
    }
    return 3;
}