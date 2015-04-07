
    def isPalindrome(x):
        if x == 0: # when x is zero
          return True

        if x < 0 or x%10 == 0: # when x is negative or ends with 0
          return False

        reverse = 0

        # Stop if reverse is greater than x or reverse == x (when x has even digits) or reverse == x/10 (when x has odd digits)

        while reverse < x: 
          last_int = x % 10
          reverse = reverse*10 + last_int
          if reverse == x or reverse == x/10:
            return True
          x = x / 10

        return False