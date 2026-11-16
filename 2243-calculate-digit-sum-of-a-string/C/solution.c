char* digitSum(char* s, int k) {
    int len = strlen(s);
    while (len > k) {
        char temp[1001];
        int idx = 0;
        for (int i = 0; i < len; i += k) {
            int sum = 0;
            for (int j = i; j < i + k && j < len; j++) {
                sum += s[j] - '0';
            }
            idx += sprintf(temp + idx, "%d", sum);
        }
        temp[idx] = '\0';
        strcpy(s, temp);
        len = strlen(s);
    }
    return s;
}