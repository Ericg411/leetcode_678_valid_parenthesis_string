class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 1:
            return False if s[0] != '*' else True

        opened = 0
        closed = 0
        stars = 0

        for c in s:
            if c == '(':
                opened += 1
            elif c == ')':
                if (opened + stars) == closed:
                    return False
                closed += 1
            elif c == '*':
                stars += 1

        diff = abs(opened - closed)
        if stars >= diff:
            return True

        return False