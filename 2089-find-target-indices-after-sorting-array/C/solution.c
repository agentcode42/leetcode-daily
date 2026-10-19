/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* targetIndices(int* nums, int numsSize, int target, int* returnSize) {
    int count_less = 0;
    int count_target = 0;
    for (int i=0;i<numsSize;i++){
        if(nums[i]<target)count_less++;
        else if(nums[i]==target)count_target++;
    }
    int* res = (int*)malloc(count_target*sizeof(int));
    for (int i=0;i<count_target;i++){
        res[i]=count_less+i;
    }
    *returnSize =count_target;
    return res;
}