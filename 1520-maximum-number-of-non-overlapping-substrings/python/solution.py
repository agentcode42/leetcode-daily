class Solution:
    def get_intervals(self,ch,s,subs)->list[str]:
        start,end = subs[ch]
        i = start
        while i<=end:
            curr_ch = s[i]
            curr_start,curr_end = subs[curr_ch]
            if curr_start <start:
                return None
            if curr_end >end:
                end= curr_end
            i+=1
        return [start,end]
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n= len(s)
        subs = {}
        for i,ch in enumerate(s):
            if ch not in subs: 
                subs[ch]=[i,i]
            subs[ch][1]=i
        
        valid_intervals = []
        for ch in subs:
            intervals = self.get_intervals(ch,s,subs)
            if intervals:
                valid_intervals.append(intervals)
        valid_intervals.sort(key=lambda x: (x[1],x[1]-x[0]))

        res = []
        last_end = -1
        for start,end in valid_intervals:
            if start>last_end:
                res.append(s[start:end+1])
                last_end = end
        return res
        