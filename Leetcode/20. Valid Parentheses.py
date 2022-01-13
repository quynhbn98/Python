# https://leetcode.com/problems/valid-parentheses/

def isValid(self, s: str) -> bool:
    ss = list(s)
    open = ['(', '[', '{']
    close = [')', ']', '}']
    if len(s) == 2:
        if s in ['()', '[]', '{}']:
            return True
        else:
            return False
    else:
        if len(s) % 2 == 1:
            return False
        else:
            for i in range(1, len(s)):
                if (ss[i - 1] == '(' and ss[i] == ')') or (ss[i - 1] == '[' and ss[i] == ']') or (
                        ss[i - 1] == '{' and ss[i] == '}'):
                    del (ss[i - 1])
                    ss.insert(0, '0')
                    del (ss[i])
                    ss.insert(1, '0')
            if ss.count('0') == len(ss):
                return True
            else:
                return False