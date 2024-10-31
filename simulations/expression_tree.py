class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


def parse_expression(expression):
    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0

    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        node = Node(operator)
        node.right = right
        node.left = left
        values.append(node)

    def parse(expression):
        values = []
        operators = []
        i = 0
        while i < len(expression):
            if expression[i] == ' ':
                i += 1
                continue
            if expression[i] == '(':
                operators.append(expression[i])
            elif expression[i] == ')':
                while len(operators) != 0 and operators[-1] != '(':
                    apply_operator(operators, values)
                operators.pop()
            elif expression[i].isalnum():  # it's a number or alphabet
                val = []
                while i < len(expression) and (expression[i].isalnum() or expression[i] == '_'):
                    val.append(expression[i])
                    i += 1
                values.append(Node(''.join(val)))
                i -= 1
            else:  # it's an operator
                while (len(operators) != 0 and
                       precedence(operators[-1]) >= precedence(expression[i])):
                    apply_operator(operators, values)
                operators.append(expression[i])
            i += 1

        while len(operators) != 0:
            apply_operator(operators, values)

        return values[0]

    return parse(expression)


# 测试表达式 A1 * (A2 + A3)
expression = "A1*(A2+A3)"
root = parse_expression(expression)


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value, end=' ')
    inorder(node.right)


# 中序遍历输出结果
inorder(root)


