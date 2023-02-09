class Solution:
    def isValid1(self, s: str) -> bool:
        stack = []
        i = 0
        while i < len(s):
            if len(s) == 0:
                if s[i] in ['(', '{', '[']:
                    stack.append(s[i])
                else:
                    return False
            else:
                if s[i] in ['(', '{', '[']:
                    stack.append(s[i])
                else:
                    if len(stack) == 0:
                        return False

                    popped = stack.pop()
                    if popped == '(' and s[i] != ')' or popped == '{' and s[i] != '}' or popped == '[' and s[i] != ']':
                        return False
            i += 1
        if len(stack) != 0:
            return False
        return True


    def isValid2(self, s: str) -> bool:
        stack = []
        left_parentheses = {
            '(': 1,
            '{': 2,
            '[': 3
        }
        right_parentheses = {
            ')': -1,
            '}': -2,
            ']': -3
        }

        if len(s) > 0:
            i = 0
            while i < len(s):
                # deal with first character
                if len(stack) == 0:
                    # character is in the left parentheses
                    if s[i] in left_parentheses:
                        stack.append(left_parentheses[s[i]])

                    # character is in the right parentheses
                    else:
                        return False
                # after first run
                else:
                    # push character into stack if read a character which is in left parentheses
                    if s[i] in left_parentheses:
                        stack.append(left_parentheses[s[i]])

                    # pop out an item from stack if read a character which is in right parentheses
                    if s[i] in right_parentheses:
                        popped_item = stack.pop()
                        if right_parentheses[s[i]] + popped_item != 0:
                            return False
                i += 1
            if len(stack) == 0:
                return True
            return False
