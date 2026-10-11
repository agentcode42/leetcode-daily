int sumOfSquares(int* nums, int numsSize) {
    int n = numsSize;
    long long res = 0;
    for (int i=0;i<n;i++){
        if (n%(i+1)==0){
            res+=nums[i]*nums[i];
        }
    }
    return res;
}