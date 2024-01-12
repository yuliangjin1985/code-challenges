class Solution:
    def calculate(self, s):    
        def calc(i):
            def process(opr, v):
                if opr == "+": stack.append(v)
                if opr == "-": stack.append(-v)
                if opr == "*": stack.append(stack.pop() * v)
                if opr == "/": stack.append(int(stack.pop() / v))
        
            num, stack, opr = 0, [], "+"
            
            while i < len(s):
                cur = s[i]
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] in "+-*/":
                    process(opr, num)
                    num, opr = 0, s[i]
                elif s[i] == "(":
                    num, j = calc(i + 1)
                    i = j - 1
                elif s[i] == ")":
                    process(opr, num)
                    return sum(stack), i + 1
                i += 1
            process(opr, num)
            return sum(stack)

        return calc(0)
    

# tests
print(Solution().calculate("(1+2)*8"))