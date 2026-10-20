int sortableIntegers(int* nums, int numsSize) {
    int n = numsSize;
    int res = 0;
    for(int k =1;k<n+1;k++){
        if (n%k) continue;
        bool flag = true;
        int prev_max = 0;
        for (int i=0;i<n;i+=k){
            int count = 0;
            int curr_max=nums[i];
            int curr_min=nums[i];
            for (int j=0;j<k;j++){
                int a= nums[i+j];
                int b = nums[i+(j+1)%k];
                if (a>b)count++;
                if (a<curr_min)curr_min=a;
                if (a>curr_max)curr_max=a;
            }
            if (count>1 || prev_max>curr_min){
                flag = false;
                break;
            }
            prev_max = curr_max;
        }
        if (flag)res+=k;
    }
    return res;
}