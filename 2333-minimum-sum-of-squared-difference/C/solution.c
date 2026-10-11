long long minSumSquareDiff(int* nums1, int nums1Size, int* nums2, int nums2Size, int k1, int k2) {
    int n = nums1Size;
    int max_diff = 0;
    int* diff = (int*)malloc(n*sizeof(int));
    for (int i=0;i<n;i++){
        diff[i]=abs(nums1[i]-nums2[i]);
        if (diff[i]>max_diff)max_diff=diff[i];
    }

    long long* freq = (long long*)calloc(max_diff+1,sizeof(long long));
    for (int i=0;i<n;i++){
        freq[diff[i]]++;
    }

    long long k = k1+k2;
    long long take = 0;
    for (int i=max_diff;i>0;i--){
        if (k<freq[i]) take =k;
        else take = freq[i];
        freq[i]-=take;
        freq[i-1]+=take;
        k-=take;
        if (k<=0)break;
    }
    long long result = 0;
    for (long long i=1;i<=max_diff;i++){
        result += (long long) i*i*freq[i];
    }
    return result;
}