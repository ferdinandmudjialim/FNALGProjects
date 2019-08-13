# Project 02
# Ferdinand Mudjialim 09/25/18


class Stack:
    def __init__(self):
        self.items = []

    def isempty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def infixToValue(infixexpr):
    numstack = Stack()
    opstack = Stack()
    order = {'≤': 0, '+': 1, '-': 1, '*': 2}  # < has lower precedence than + & - and so on
    infix = infixexpr.split()
    for i in infix:
        if i.isdigit():
            numstack.push(i)
        elif i in order.keys():
            if not opstack.isempty():
                op = opstack.peek()
                while not opstack.isempty() and order[op] >= order[i]:
                    result = None
                    num2 = int(numstack.pop())
                    num1 = int(numstack.pop())

                    if op == "≤":
                        result = (num1 <= num2)
                    if op == "+":
                        result = (num1 + num2)
                    if op == "-":
                        result = (num1 - num2)
                    if op == "*":
                        result = (num1 * num2)

                    opstack.pop()
                    numstack.push(result)
                    if not opstack.isempty():
                        op = opstack.peek()
                else:
                    opstack.push(i)
            else:
                opstack.push(i)

    while not opstack.isempty():
        op = opstack.pop()
        result = None
        num2 = int(numstack.pop())
        num1 = int(numstack.pop())

        if op == "≤":
            result = (num1 <= num2)
        if op == "+":
            result = (num1 + num2)
        if op == "-":
            result = (num1 - num2)
        if op == "*":
            result = (num1 * num2)
        numstack.push(result)
    return numstack.pop()


print(infixToValue("14 - 3 * 2 + 7"))
print(infixToValue("14 ≤ 4 - 3 * 2 + 7"))
print(infixToValue("15 + 16 - 2 + 7 * 3 * 2 - 14"))
