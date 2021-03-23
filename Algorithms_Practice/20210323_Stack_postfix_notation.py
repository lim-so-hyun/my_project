class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(S):
    opStack = ArrayStack()
    answer = ''

    for i in S:
        if i == '(':
            opStack.push(i)
        elif i == ')':
            while opStack.peek() != '(':
                answer += opStack.pop()
            opStack.pop()
        elif i in prec:
            if opStack.isEmpty():
                opStack.push(i)
            elif prec[i] > prec[opStack.peek()]:
                opStack.push(i)
            else:
                while not opStack.isEmpty() and prec[i] <= prec[opStack.peek()]:
                    answer += opStack.pop()
                opStack.push(i)

        else:
            answer += i

    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer