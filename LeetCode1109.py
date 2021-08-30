class Solution:
    def corpFlightBookings(self, bookings, n):
        d = [0 for _ in range(n+1)]
        for booking in bookings:
            d[booking[0]-1] += booking[2]
            d[booking[1]] -= booking[2]
        for i in range(1,n):
            d[i] = d[i] + d[i-1]
        return d[:-1]
