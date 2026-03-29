class TreeNode:
    def __init__(self, data,):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)
        '''if self.children:
            for idx,child in enumerate(self.children):
                if idx == int(level):
                    break
                child.print_tree(level)'''


    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_country_tree():
    global_c = TreeNode("Global")

    country_1 = TreeNode("India")
    country_2= TreeNode("USA")
    global_c.add_child(country_1)
    global_c.add_child(country_2)

    inc_cities_1 = TreeNode("Gujarat")
    inc_cities_2 = TreeNode("Karnataka")
    country_1.add_child(inc_cities_1)
    country_1.add_child(inc_cities_2)

    usa_cities_1 = TreeNode("New Jersey")
    usa_cities_2 = TreeNode("California")

    country_2.add_child(usa_cities_1)
    country_2.add_child(usa_cities_2)

    inc_cities_1.add_child(TreeNode("Ahmedabad"))
    inc_cities_1.add_child(TreeNode("Baroda"))

    inc_cities_2.add_child(TreeNode("Bengaluru"))
    inc_cities_2.add_child(TreeNode("Mysore"))

    usa_cities_1.add_child(TreeNode("Princeton"))
    usa_cities_1.add_child(TreeNode("Trenton"))

    usa_cities_2.add_child(TreeNode("San Francisco"))
    usa_cities_2.add_child(TreeNode("Mountain View"))
    usa_cities_2.add_child(TreeNode("Palo Alto"))

    return global_c


if __name__ == '__main__':
    root_node = build_country_tree()
    root_node.print_tree(1)
    root_node.print_tree(2)
    root_node.print_tree(3)