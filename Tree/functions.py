import operator

class BinaryTree(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insertLeft(self, b):

        if not self.left:
            self.left = b
        else:
            b.left = self.left
            self.left = b


    def insertRight(self, b):

        if not self.right:
            self.right = b
        else:
            b.right = self.right
            self.right = b

    def getRootVal(self):
        return self.value

    def setRootVal(self, value):
        self.value = value

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def __str__(self):
        return "(%s, %s, %s)" % (self.value, self.left, self.right)


def parseTree(expression):

    elements = expression.split()
    print(elements)
    top = BinaryTree(-1)
    current_node = top

    for e in elements:
        if e == '(':
            c = BinaryTree(-1)
            c.setParent(current_node)
            current_node.insertLeft(c)
            current_node = c
        elif e in ['+','-','/','*']:
            current_node.setRootVal(e)
            c = BinaryTree(-1)
            c.setParent(current_node)
            current_node.insertRight(c)
            current_node = c
        elif e.isdigit():
            current_node.setRootVal(int(e))
            current_node = current_node.getParent()
        elif e == ')':
            current_node = current_node.getParent()

    return top

pt = parseTree("( ( 10 + 5 ) * 3 )")
print(pt)

def evaluateTree(tree):

    opes = {'+':operator.add ,'-':operator.sub,'/':operator.div,'*':operator.mul}

    left = tree.getLeftChild()
    right = tree.getRightChild()

    if left and right:
        f = opes[tree.getRootVal()]
        return f(evaluateTree(left), evaluateTree(right))
    else:
        return tree.getRootVal()

value = evaluateTree(pt)
print(value)

def preorder(tree):

    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

print('preorder')
preorder(pt)

def inorder(tree):

    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

print('inorder')
inorder(pt)

def postorder(tree):

    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

print('postorder')
postorder(pt)

def printexp(tree):

    s = ""
    if tree:
        left = tree.getLeftChild()
        right = tree.getRightChild()
        if left and right:
            paren_start = "("
            paren_end = ")"
        else:
            paren_start = ""
            paren_end = ""

        if tree:
            s = paren_start + printexp(tree.getLeftChild())
            s = s + str(tree.getRootVal())
            s = s + printexp(tree.getRightChild()) + paren_end

    return s

print(printexp(pt))

# r = BinaryTree(3)
# r.insertLeft(4)
# r.insertLeft(5)
# r.insertRight(6)
# r.insertRight(7)
# l = r.getLeftChild()
# print(l)
#
# l.setRootVal(9)
# print(r)
# l.insertLeft(11)
# print(r)
# print(r.getRightChild().getRightChild())