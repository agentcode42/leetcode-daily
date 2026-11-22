bool checkString(char* s) {
    bool flag_a = false;
    bool flag_b = false;
    for(int i = 0; s[i]!='\0';i++){
        if (s[i]=='a'){
            flag_a = true;
            if (flag_b)return false;
        }
        else flag_b = true;
    }
    return true;
}