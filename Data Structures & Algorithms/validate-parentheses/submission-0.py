class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for c in s:

            if c in close:
                stack.append(c)

            else:
                if not stack:
                    return False

                top = stack.pop()

                if close[top] != c:
                    return False

        return len(stack) == 0        