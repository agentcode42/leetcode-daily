class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def year_day (arr):
            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            arr = arr.split("-")
            days = sum(months[:int(arr[0])-1]) + int(arr[1])
            return days
        
        alice_a = year_day(arriveAlice)
        alice_l = year_day(leaveAlice)
        bob_a = year_day(arriveBob)
        bob_l= year_day(leaveBob)
        match_a = max(alice_a,bob_a)
        match_l = min(alice_l,bob_l)

        return max(0,match_l - match_a +1)
        
        
        
        