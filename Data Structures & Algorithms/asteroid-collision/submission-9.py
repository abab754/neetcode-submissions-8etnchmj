class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 1
        stack.append(asteroids[0])
        while i < len(asteroids):
            cur = asteroids[i]
            if len(stack) == 0:
                stack.append(cur)
                i+=1
                continue
            if stack[-1] < 0 or (cur > 0 and stack[-1] > 0):
                stack.append(cur)
                i+=1
            else:
                cur_abs = abs(cur)
                while len(stack) > 0 and stack[-1] > 0 and cur_abs > abs(stack[-1]):
                    stack.pop()

                if len(stack) == 0:
                    stack.append(cur)
                    i+=1
                elif stack[-1] < 0:
                    continue
                else:
                    if cur_abs == abs(stack[-1]):
                        i+=1
                        stack.pop()
                    elif cur_abs < abs(stack[-1]):
                        i+=1

        return stack