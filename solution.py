class Solution:
    def checkValidString(self, s: str) -> bool:
        balance = 0
        for c in s:
            if c == '(' or c == '*':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False

        balance = 0
        for c in s[::-1]:
            if c == ')' or c == '*':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False    
        
        return True