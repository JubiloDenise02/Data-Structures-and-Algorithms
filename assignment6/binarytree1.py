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
    
    #method that return the list of elements in binary tree in specific order       
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
        

#method that takes elements as an input and build a tree
def build_tree(elements):
    # assigning the first element as a root node
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i]) #child method to build a tree

    return root

#main
if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))
    
    #alphabetical order
    print(country_tree.in_order_traversal())
    
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print("sorted list:", numbers_tree.in_order_traversal())