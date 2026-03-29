class BInarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            # add data in left sub Tree
           if self.left:
               self.left.add_child(data)
           else:
              self.left = BInarySearchTreeNode(data)
        else:
            #add data in Right Sub Tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BInarySearchTreeNode(data)


    def in_order_traversal(self):
        elements = []
        # Visit left Tree
        if self.left :
           elements += self.left.in_order_traversal()
        # Visit Base Node
        elements.append(self.data)
        # Visit Right Tree
        if self.right:
            elements += self.right.in_order_traversal()

        return  elements

    def search(self,val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val) #Recursion func calling itself
            else:
                return False
            # Val might be left sub Tree
        if val > self.data:
            # val might be right sub Tree
            if self.right:
                return self.right.search(val)  # Recursion func calling itself
            else:
                return False


def build_tree(elements):
    root = BInarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__" :
    numbers = [17,4,1,20,9,23,18,34,18,4]
    numbers_tree =  build_tree(numbers)
   # print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(200))

    countries = ["India","Pakistan","Germany","USA","China","India","UK"]
    country_tree = build_tree(countries)

    print(country_tree.in_order_traversal())
    print("UK in the list ?",country_tree.search("UK"))
    print("Sweden  in the list ?",country_tree.search("SWEDEN"))