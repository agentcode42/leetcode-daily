int longestMonotonicSubarray(int* nums, int numsSize) {
    int inc_count = 1;
    int dec_count = 1;
    int max_count = 1;
    for (int i = 1;i<numsSize;i++){
        if (nums[i]>nums[i-1]){
            inc_count ++;
            dec_count = 1;
        }
        else if (nums[i]<nums[i-1]){
            inc_count=1;
            dec_count ++;
        }
        else{
            inc_count = 1;
            dec_count = 1;
        }
        int max = dec_count;
        if (inc_count> max) max = inc_count;
        if (max_count< max) max_count = max;
    }
    return max_count;
}