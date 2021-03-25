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


def splitTokens(exprStr):   # 문자열로 들어온 중위계산식을 숫자, 연산자 각각을 원소로 갖는 list로 변환하기 위한 함수
    tokens = []
    val = 0
    valProcessing = False # 초기 설정
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':    # 숫자 나오면, 해당 정수 뭉탱이로 int 자료형으로 list에 넣어야 해서 숫자 끝날 때까지 ValProcessing=True로 해두기
            val = val * 10 + int(c)   # 숫자 뭉텅이 하나의 정수로 인식 시킬 수 있는 계산식
            valProcessing = True
        else:   # 연산자 나오면
            if valProcessing:   # 방금까지 숫자였다는 뜻이고, 이제 연산자 나왔으니 숫자 끝! list에 원소로 val 추가
                tokens.append(val)
                val = 0  # reset
            valProcessing = False  # 숫자 아니니까 false로 돌려두기
            tokens.append(c)   # 연산자는 그대로 리스트에 문자열로 넣으면 됨.
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):    # 리스트로 변환되어있는 중위표현식을 후위표현식으로 변환하자
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()   # stack 자료구조 이용하는건 지난번과 동일
    postfixList = []   # 이것도 list 형태로 받을거니까 미리 생성해두자. 지난번과 달라진점!

    for i in tokenList:
        if i == '(':
            opStack.push(i)
        elif i == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())  # 지난번엔 문자열로 출력할거라 문자열 + 로 표현했지만 이번엔 list에 append하는 방식
            opStack.pop()
        elif i in prec:
            if opStack.isEmpty():
                opStack.push(i)
            elif prec[i] > prec[opStack.peek()]:
                opStack.push(i)
            else:
                while not opStack.isEmpty() and prec[i] <= prec[opStack.peek()]:
                    postfixList.append(opStack.pop())
                opStack.push(i)
        else:
            postfixList.append(i)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):  # 이제 list 꼴로 정리되어있는 후위표현식 가지고 계산 해서 값 내는 코드 구현
    opStack = ArrayStack()  # stack 이용하자
    for c in tokenList:
        if type(c) == int:   # list 내에 정수형과 문자열 형 있음. 정수형이면 그대로 push하면 됨.
            opStack.push(c)
        else:  # 연산자, 즉 문자열일 때
            sec = opStack.pop()  # 첫번째 pop한게 사실상은 더 늦게 들어간 원소니까 -, / 연산할 때에는 뒤로 들어가야해서 second라고 함.
            first = opStack.pop()
            if c == '+':
                result = sec + first
            if c == '*':
                result = sec * first
            if c == '-':
                result = first - sec
            if c == '/':
                result = first / sec
            opStack.push(result)

    return opStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

print(solution("3+5-1"))
print(solution("(1+2)*(3+4)"))
print(solution("7-(9-(3+2))"))