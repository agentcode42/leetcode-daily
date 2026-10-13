long long maxAlternatingSum(int* nums, int numsSize) {
 int max_val = 40000;
 int freq[40001] ={0};
 for (int i=0;i<numsSize;i++){
    freq[abs(nums[i])]++;
 }
 long long score = 0;
 int processed = 0;
 int k = numsSize/2;

 for (int i = 0;i<=max_val;i++){
    while (freq[i]>0){
        long long sq = (long long) i*i;
        if (processed<k){
            score-= sq;
        }
        else{
            score+=sq;
        }
        processed++;
        freq[i]--;
    }
 }
 return score;
}