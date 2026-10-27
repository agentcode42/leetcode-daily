/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** createGrid(int m, int n, int* returnSize) {
    char** res = malloc(m*sizeof(char*));
    res[0]=malloc((n+1)*sizeof(char));
    memset(res[0],'.',n);
    res[0][n]='\0';

    for (int i=1;i<m;i++){
        res[i]=malloc((n+1)*sizeof(char));
        memset(res[i],'#',n-1);
        res[i][n-1]='.';
        res[i][n]='\0';
    }
    *returnSize=m;
    return res;
}