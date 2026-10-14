char* maxSumOfSquares(int num, int sum) {
    if(sum>num*9) return "";

    char* res = (char*)malloc((num+1)*sizeof(char));

    for (int i=0;i<num;i++){
        int digit = (sum<9)?sum:9;
        res[i]='0'+digit;
        sum-=digit;
    }
    res[num]='\0';
    return res;
}