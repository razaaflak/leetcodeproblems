class Solution(object):
    def romanToInt(self, s):
        vals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        s = s[::-1]
        sum = vals[s[0]]
        for i in range(1, len(s)):
            if vals[s[i]] >= vals[s[i-1]]:
                sum += vals[s[i]]
            else:
                sum -= vals[s[i]]

        return sum
        
for i in range(10,-1,-1):
    print(i)