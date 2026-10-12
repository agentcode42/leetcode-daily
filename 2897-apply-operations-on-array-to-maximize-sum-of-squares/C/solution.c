int maxSum(int* nums, int numsSize, int k) {
    int count[32] = {0};
    long long res = 0;
    long long MOD = 1000000007;
   
    for (int j = 0; j < numsSize; j++) {
        int val = nums[j];
        for (int i = 0; i < 32; i++) {
            if (val & (1LL << i)) {
                count[i]++;
            }
        }
    } 


    for (int j = 0; j < k; j++) {
        long long x = 0;
        for (int i = 31; i >= 0; i--) {
            if (count[i] > 0) {
                x |= (1LL << i);
                count[i]--;    
            }
        }
        res = (res + (x * x) % MOD) % MOD;
    }   
    return (int)res;   
}
