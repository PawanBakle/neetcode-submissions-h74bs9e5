import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        eval_res = 0
        ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
        for token in range(len(tokens)):
            # check if token is a number
            # if number just push it 
            if tokens[token] in ops:
                # pop last 2 numbers as operands
                val2 = stack.pop()
                val1 = stack.pop()
                opr = ops[tokens[token]]
                if opr == operator.truediv:
                    eval_res = math.trunc(val1/val2)
                else:
                    eval_res = opr(val1,val2)
                stack.append(eval_res)
                
            else:
                tok = int(tokens[token])

                stack.append(tok)
        if len(tokens) == 1:
            return int(tokens[-1])
        return eval_res



