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

    def pre_order_traversal(self): # Ex
        elements = []
        # Visit Base Node
        elements.append(self.data)

        # Visit Left Tree
        if self.left:
            elements += self.left.pre_order_traversal()

        # Visit Right Tree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self): #Ex
        elements = []
        # Visit Left Tree
        if self.left:
            elements += self.left.pre_order_traversal()

        # Visit Right Tree
        if self.right:
            elements += self.right.pre_order_traversal()

        # Visit Base Node
        elements.append(self.data)

        return elements

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


    def find_max(self): #Ex
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self): #Ex
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self): #Ex
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum


def build_tree(elements):
    root = BInarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__" :
    numbers = [17,4,1,20,9,23,18,34,18,4]
    numbers_tree =  build_tree(numbers)
    print("In Order",numbers_tree.in_order_traversal())
    print("Pre Order",numbers_tree.pre_order_traversal())
    print("Post Order",numbers_tree.post_order_traversal())
    print("Min:", numbers_tree.find_min())
    print("Max:", numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("Search Element",numbers_tree.search(200))

    countries = ["India","Pakistan","Germany","USA","China","India","UK"]
    country_tree = build_tree(countries)

    print(country_tree.in_order_traversal())
    print("UK in the list ?",country_tree.search("UK"))
    print("Sweden  in the list ?",country_tree.search("SWEDEN"))
