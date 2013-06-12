class Tree:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def add_left(self,El):
        self.left=El
        El.parent = self

    def add_right(self,El):
        self.right=El
        El.parent = self

    def __repr__(Tree):
        return "<El, value=%s>" % self.value

    def subtree(self, ntabs = 0):
        for i in range(ntabs):
            print "\t",
        print self.value
        if self.left != None:
            self.left.subtree(ntabs + 1)
        if self.right != None:
            self.right.subtree(ntabs + 1)

    def graphviz(self):
        if self.parent == None:
            parent_value = None
        else:
            parent_value = self.parent.value
        print parent_value, "->", self.value
        if self.left != None:
            self.left.graphviz()
        if self.right != None:
            self.right.graphviz()

    def add_value(self,El):
        if El.value>self.value:
            if self.right==None:
                self.add_right(El)
            else:
                self.right.add_value(El)
        if El.value<self.value:
            if self.left==None:
                self.add_left(El)
            else:
                self.left.add_value(El)

    def delete_el(self, value):
       if self.value == value:
           if self.parent != None:
               if self.value > self.parent.value:
                   self.parent.right = None
               else:
                   self.parent.left = None
               if self.right != None:
                   self.parent.add_value(self.right)
               if self.left != None:
                   self.parent.add_value(self.left)
       else:
         if self.left != None:
            self.left.delete_el(value)
         if self.right != None:
             self.right.delete_el(value)

    def search(self, El):
        if self.value < El:
            if self.right != None:
                self.right.search(El)
        elif self.value > El:
            if self.left != None:
                self.left.search(El)
        if self.value == El:
            print "OK. The item is found"


print "Enter the length of the array:"
N=input()
print("\n")
Count=0
M=[]
for Count in range(N):
    X=input()
    M=M+[X]
    Count+=1
Count=0
Tree=Node(M[0])
while Count < len(M)-1:
    Count+=1
    Tree.add_value(Node(M[Count]))
