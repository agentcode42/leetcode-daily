int sortPermutation(int* nums, int numsSize) {
    int res = -1;
    for (int i=0;i<numsSize;i++){
        if (nums[i]==i)continue;
        res = res&nums[i];
    }
    return res==-1 ?0:res;
}