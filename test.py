#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-05-24 15:16
# @Author  : xxd
# @File    : test.py

class Node:

    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

#统计树中节点

def countNode(t):
    if t is None:
        return 0
    else:
        return 1+countNode(t.left)+countNode(t.right)
#求二叉树里所有数值和
def sumNode(t):
    if t is None:
        return 0
    else:
        return t.data+ sumNode(t.left) + sumNode(t.right)

#前序遍历
def preOrder(t):
    if t is None:
        return
    print (t.data)
    preOrder(t.left)
    preOrder(t.right)

#中序遍历
def midOrder(t):
    if t is None:
        return

    midOrder(t.left)
    print(t.data)
    midOrder(t.right)


# 后序遍历
def postOrder(t):
    if t is None:
        return

    postOrder(t.left)
    postOrder(t.right)
    print(t.data)

#非递归实现前序遍历
def preOrderNonRec(Node):
    if Node == None:
        return
    #用数组当栈
    stack = []
    while Node or stack:
        while Node:
            # 从根节点开始，一直找它的左子树
            print(Node.data)
            #将右子树压入栈中
            stack.append(Node)
            #一直往下找左子树
            Node = Node.left
        # while结束表示当前节点Node为空，即前一个节点没有左子树了
        # 栈中开始弹出上右子树，再重复前面步骤
        Node = stack.pop()
        Node=Node.right



#非递归实现中序遍历

# 中序的非递归遍历与先序的非递归遍历类似。先序遍历是先访问节点，然后再将节点入栈，
# 后中序遍历则是先入栈，然后节点弹出栈后再访问。
def midOrderNonRec(Node):
    if Node == None:
        return
    #用数组当栈
    stack = []
    while Node or stack:
        while Node:
            # 从根节点开始，一直找它的左子树
            #将父节点压入栈中
            stack.append(Node)
            #一直往下找左子树
            Node = Node.left
        # while结束表示当前节点Node为空，即前一个节点没有左子树了
        # 栈中开始弹出，再重复前面步骤
        Node = stack.pop()
        print(Node.data)
        Node=Node.right

#非递归实现后序遍历
def postOrderNonRec(Node):
    if Node == None:
        return
    #用数组当栈
    stack = []
    while Node or stack:
        while Node:
            # 从根节点开始，一直找它的左子树
            stack.append(Node)
            #能左就左，否则就向右走一步
            Node = Node.left if Node.left is not None else Node.right

        # 到下面都没有左子树和右子树的节点后，栈中开始弹出

        Node = stack.pop() #栈顶就是当前应访问节点
        print(Node.data)
        #栈不空且当前节点是栈顶的左子节点，那么应当继续去访问栈顶的右子节点
        if len(stack)!=0 and stack[-1].left==Node:
            Node=stack[-1].right
        else:
            #没有右子树或右子树遍历完毕，强迫退栈
            Node=None

def BFS(Node):
    if Node == None:
        return
    quene = []
    quene.append(Node)
    while quene:
        Node = quene.pop(0)
        print(Node.data)
        if Node.left:
            quene.append(Node.left)
        if Node.right:
            quene.append(Node.right)

if __name__ == '__main__':
 t=Node(1,Node(2),Node(3))
 # # 统计树中节点
 # print(countNode(t))
 # # 求二叉树里所有数值和
 # print (sumNode(t)
 # 前序遍历
 # preOrder(t)
 # # 中序遍历
 # midOrder(t)
 # # 后序遍历
 # postOrder(t)
 print("前序遍历")
 preOrderNonRec(t)
 print("中序遍历")
 midOrderNonRec(t)
 print("后序遍历")
 postOrderNonRec(t)
 print("宽度优先遍历")
 BFS(t)