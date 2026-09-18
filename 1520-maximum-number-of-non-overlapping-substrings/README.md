# LeetCode 1520 — Maximum Number of Non-Overlapping Substrings

[LeetCode Problem](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/)

## Problem

Given a string `s` containing only lowercase English letters, find the maximum number of non-empty substrings such that:

* Every occurrence of a character is included whenever that character appears in the substring.
* The chosen substrings do not overlap.
* If multiple answers contain the same maximum number of substrings, choose the one with the minimum total length.

## Approach

The key idea is to build **valid closed intervals** for characters and then use a greedy interval scheduling strategy.

A substring is valid only when every character inside it has all of its occurrences contained inside the substring.

### 1. Find the first and last occurrence of every character

For every character, store:

```text
[first occurrence, last occurrence]
```

For example, for:

```text
s = "abac"
```

we get:

```text
a -> [0, 2]
b -> [1, 1]
c -> [3, 3]
```

These are the smallest possible intervals for each character.

### 2. Expand each interval

Starting from a character's first occurrence, scan through its current interval.

Whenever we find another character inside the interval:

* Its **first occurrence** must not be before our current start.
* Its **last occurrence** must be included, so we extend the end if necessary.

For example, if our current interval contains `b` and `b` appears again later, the interval must expand to include that occurrence too.

We continue expanding until the entire interval is closed.

### 3. Reject invalid intervals

Suppose we are building an interval starting at index `start`, but we encounter a character whose first occurrence is before `start`.

That means this character already appeared outside our interval, so we cannot create a valid substring using this starting point.

In that case, we discard the interval.

### 4. Greedy selection

After generating all valid intervals, the remaining problem is simply:

> Select the maximum number of non-overlapping intervals.

This is the classic interval scheduling problem.

We sort the intervals by:

```text
(end, length)
```

The earliest ending interval is chosen first because it leaves the most room for the remaining intervals.

The length is used as a secondary key to prefer smaller intervals when the ending position is the same.

Finally, we iterate through the sorted intervals and take an interval whenever its start is after the end of the previously selected interval.

## Python Solution

```python
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
        
```

## Complexity Analysis

### Time Complexity: `O(N)`

Finding the first and last occurrence of every character takes `O(N)`.

For each of the at most 26 lowercase characters, we may scan part of the string while expanding its interval.

So the interval construction takes:

```text
O(26 × N) = O(N)
```

Sorting at most 26 intervals takes:

```text
O(26 log 26) = O(1)
```

Therefore, the overall time complexity is:

```text
O(N)
```

### Space Complexity: `O(N)`

The dictionary stores information for at most 26 characters, which is `O(1)`.

The list of valid intervals also contains at most 26 intervals, so it is `O(1)`.

However, the result can contain substrings whose total length is `O(N)`.

Therefore, including the returned result, the overall space complexity is:

```text
O(N)
```


