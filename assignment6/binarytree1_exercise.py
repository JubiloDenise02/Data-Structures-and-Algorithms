#general tree which node can have any of the elements  
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        #leftsearchtree
        self.left = None #elements are less than the current node
        #rightsearchtree
        self.right = None #elements are greater than the current node
     
    #method of checking the value 
    def add_child(self, data):
        if data == self.data: #see if the value already exists
            return #node already exist

        #if the data is less than self.data
        if data < self.data: 
            #add data in left subtree
            if self.left: #check if the left element has value
                self.left.add_child(data) #call child method (recursion)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #add data in right subtree
            if self.right: #check if the right element has value
                self.right.add_child(data) #call child method (recursion)
            else:
                self.right = BinarySearchTreeNode(data)
    
    #method to search some value
    def search(self,val):
        if self.data == val: #check if the self.data is the same as the value
            return True

        if val < self.data:
            #val might be on left subtree
            if self.left: #check if it has any content 
                return self.left.search(val) #search method (recursion)
                
            else:
                return False
        
        if val > self.data:
            #val might be on right subtree
            if self.right: #check if it has any content 
                return self.right.search(val) #search method (recursion)
            else:
                return False
    
    #method for inorder       
    def in_order_traversal(self):
        #add list 
        elements = []
        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #visit base node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    #method for preorder
    def pre_order_traversal(self):
        # visit base node
        elements = [self.data]
        
        #visit left tree
        if self.left:
            elements += self.left.pre_order_traversal()
        
        #visit right tree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    #method for postorder   
    def post_order_traversal(self):
        #add list 
        elements = []
        
        #visit left tree
        if self.left:
            elements += self.left.post_order_traversal()
        
        #visit right tree
        if self.right:
            elements += self.right.post_order_traversal()

        #visit base node
        elements.append(self.data)

        return elements
    
    #method to find the highest or largest number
    def find_max(self):
        #since the rule is all elements that is greater than the current node
        #its always on the right subtree
        if self.right is None:
            return self.data
        return self.right.find_max() 
    
    #method to find the lowest or smallest number
    def find_min(self):
        #since the rule is all elements that is less than the current node
        #its always on the left subtree
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    #method to sum up all the elements in binary tree
    def calculate_sum(self):
        #check if the left tree has value and sum up all in the left
        left_sum = self.left.calculate_sum() if self.left else 0 
        #check if the right tree has value and sum up all in the right
        right_sum = self.right.calculate_sum() if self.right else 0
        #sum up all
        return self.data + left_sum + right_sum


#method that takes elements as an input and build a tree
def build_tree(elements):
    # assigning the first element as a root node
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i]) #child method to build a tree

    return root

#main
if __name__ == '__main__':
    print()
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    
    numbers_tree = build_tree(numbers)
    
    print("Numbers:", numbers)
    print()
    print("Min/smallest/lowest:",numbers_tree.find_min())
    print("Max/largest/highest:",numbers_tree.find_max())
    print("Sum/total:", numbers_tree.calculate_sum())
    print()
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())
    
    