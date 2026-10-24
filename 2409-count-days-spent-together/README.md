# 2409. Count Days Spent Together

**LeetCode:** [2409. Count Days Spent Together](https://leetcode.com/problems/count-days-spent-together/)  
**Difficulty:** Easy  
**Language:** Python

## 1. Problem Summary

Alice and Bob each have an arrival date and a departure date, represented in `MM-DD` format.

Both dates are inclusive, meaning the arrival day and departure day count as days spent at a location.

Our task is to calculate how many days Alice and Bob are present at the same time.

If their stays do not overlap, return `0`.

## 2. Intuition

Instead of comparing dates month by month, we can convert every date into its corresponding day number within the year.

For example, January 1 is day 1, while February 1 is day 32 because January has 31 days.

Once all four dates are converted into day numbers, the problem becomes an interval-overlap problem.

We can find the overlapping interval using two simple operations:

- The later arrival date is the beginning of the overlap.
- The earlier departure date is the end of the overlap.

If the overlapping interval is valid, its length is the number of days spent together. Otherwise, the answer is zero.

## 3. Approach

### Step 1: Convert dates into day numbers

Create a helper function called `year_day()`.

- Split the date into its month and day.
- Store the number of days in each month.
- Add the days from all previous months to the current day.

For example, `03-15` becomes:

31 days in January + 28 days in February + 15 days in March = **74**.

### Step 2: Convert all four dates

Convert Alice's arrival and departure dates and Bob's arrival and departure dates into day numbers.

This gives us four integers that are easy to compare.

### Step 3: Find the overlapping interval

Calculate the later arrival:

`match_a = max(alice_a, bob_a)`

Calculate the earlier departure:

`match_l = min(alice_l, bob_l)`

These two values define the possible period during which both people are present.

### Step 4: Calculate the number of overlapping days

Because both endpoints are inclusive, calculate:

`match_l - match_a + 1`

However, if the departure of the overlapping interval occurs before its arrival, there is no overlap. Therefore, use `max(0, ...)` to ensure the result is never negative.

## 4. Python Solution

```python
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                          arriveBob: str, leaveBob: str) -> int:

        def year_day(arr):
            months = [31, 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]

            arr = arr.split("-")
            days = sum(months[:int(arr[0]) - 1]) + int(arr[1])

            return days

        alice_a = year_day(arriveAlice)
        alice_l = year_day(leaveAlice)
        bob_a = year_day(arriveBob)
        bob_l = year_day(leaveBob)

        match_a = max(alice_a, bob_a)
        match_l = min(alice_l, bob_l)

        return max(0, match_l - match_a + 1)
```

## 5. Examples

### Example 1

**Input:**

```text
arriveAlice = "08-15"
leaveAlice  = "08-18"
arriveBob   = "08-16"
leaveBob    = "08-19"
```

**Explanation:**

- Alice stays from August 15 to August 18.
- Bob stays from August 16 to August 19.
- Their overlapping dates are August 16, 17, and 18.

The later arrival is August 16, and the earlier departure is August 18.

Days together = 18 − 16 + 1 = **3**.

**Output:**

```text
3
```

### Example 2

**Input:**

```text
arriveAlice = "10-01"
leaveAlice  = "10-31"
arriveBob   = "11-01"
leaveBob    = "12-31"
```

**Explanation:**

Alice leaves on October 31, but Bob arrives on November 1. Their stays do not overlap.

The calculated overlap length is negative, so `max(0, ...)` returns zero.

**Output:**

```text
0
```

### Example 3

**Input:**

```text
arriveAlice = "06-01"
leaveAlice  = "06-10"
arriveBob   = "06-10"
leaveBob    = "06-20"
```

**Explanation:**

Both Alice and Bob are present on June 10. Since the arrival and departure dates are inclusive, this single shared day counts.

**Output:**

```text
1
```

## 6. Complexity Analysis

**Time Complexity: O(1)**

Each date contains a fixed-size month and day. The month list has only 12 elements, so converting the four dates takes constant time.

**Space Complexity: O(1)**

The month list and date components require a constant amount of additional space.

## 7. Key Takeaway

The main idea is to convert dates into day numbers and treat each person's stay as an interval.

Using `max()` to find the later arrival, `min()` to find the earlier departure, and an inclusive interval-length calculation makes the solution simple and efficient.

**Important edge case:** Always check whether the intervals overlap. If they do not, return zero instead of a negative number.