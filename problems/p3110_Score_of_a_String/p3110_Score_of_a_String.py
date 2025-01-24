from utils.my_abs import my_abs

class Solution:

    def scoreOfString(self, s: str) -> int:
        sum = 0
        for index in range(len(s) - 1):
            current_letter = s[index]
            next_letter = s[index + 1]
            sum += my_abs(ord(current_letter) - ord(next_letter))
        
        return sum
    