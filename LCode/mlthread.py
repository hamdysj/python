class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        num = 0
        temp = "I"

        for numeral in s[::-1]:
            if romans[numeral] < romans[temp]:
                num -= romans[numeral]
            else:
                num += romans[numeral]
            temp = numeral

        return num


sol = Solution()
print(sol.romanToInt("CMIX"))
