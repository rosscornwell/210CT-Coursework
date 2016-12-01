#include <iostream>
 
class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)
 
#IMPORTANT SUBROUNTINE HERE!!!
def in_order(tree):
    current = tree
    s = []
    done = 0
    while (not done):
        if current != None: #checks if the tree is empty
            s.append(current)#adds the tree to the list
            current = current.left#moves to the left side
        else:
            if len(s) >0:#list already have values
                current = s.pop()#pop the last value to 'current'
                print(current.value)
                current = current.right #moves to the right side
            else:
                done = 1#when finished end while loop
 
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
