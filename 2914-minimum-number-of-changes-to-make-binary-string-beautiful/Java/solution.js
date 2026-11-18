/**
 * @param {string} s
 * @return {number}
 */
var minChanges = function(s) {
    let n = s.length;
    let res = 0;
    for(let i =0;i<n;i+=2){
        if(s[i]!=s[i+1]){
            res+=1;
        }
    }
    return res;
};