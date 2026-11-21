class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # Step 1: Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            sign = 1
            i += 1

        # Step 3: Convert digits
        num = 0

        while i < n and s[i] >= '0' and s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            num = num * 10 + digit
            i += 1

        num = num * sign

        # Step 4: Check 32-bit range
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1

        return num