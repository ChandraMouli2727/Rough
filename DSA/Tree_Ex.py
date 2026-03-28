from tarfile import data_filter


class TreeNode():

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def extract_values(a, type_3):
    b = ''
    start_pos = 0
    end_pos = -1
    if type_3 == "name":
        end_pos = a.find("(")
    elif type_3 == "designation":
        start_pos = a.find("(")
        start_pos += 1
        end_pos = a.find(")")

    b = a[start_pos:end_pos]
    return b


def business_model(type_2):
    # root1 = extract_values("Nilupul (CEO) ",type_2)
    # print(root1)
    '''root = TreeNode( "Nilupul (CEO)" if type_2 == 'both' else extract_values("Nilupul (CEO)", type_2))
    cto = TreeNode("Chinmay (CTO)")
    hr_lead = TreeNode("Gels (HR LEAD)")
    cto_vis = TreeNode("Vishwa (Infrastructure Head")
    cto_aam=TreeNode("Aamir  (Application Head")
    cto.add_child(cto_vis)
    cto.add_child(cto_aam)
    cto_vis.add_child( TreeNode("Dhaval (Cloud Manager"))
    cto_vis.add_child( TreeNode("Abhijit (App Manager"))
    hr_lead.add_child(TreeNode("Peter (Recruitment Manager)"))
    hr_lead.add_child(TreeNode("Waqas  (Policy Manager"))
    root.add_child(cto)
    root.add_child(hr_lead)'''
    root = TreeNode("Nilupul (CEO)" if type_2 == 'both' else extract_values("Nilupul (CEO)", type_2))
    cto = TreeNode("Chinmay (CTO)" if type_2 == 'both' else extract_values("Chinmay (CTO)", type_2))
    hr_lead = TreeNode("Gels (HR LEAD)" if type_2 == 'both' else extract_values("Gels (HR LEAD)", type_2))
    cto_vis = TreeNode(
        "Vishwa (Infrastructure Head)" if type_2 == 'both' else extract_values("Vishwa (Infrastructure Head)", type_2))
    cto_aam = TreeNode(
        "Aamir (Application Head)" if type_2 == 'both' else extract_values("Aamir (Application Head)", type_2))

    cto.add_child(TreeNode(
        "Vishwa (Infrastructure Head)" if type_2 == 'both' else extract_values("Vishwa (Infrastructure Head)", type_2)))
    cto.add_child(TreeNode(
        "Aamir (Application Head)" if type_2 == 'both' else extract_values("Aamir (Application Head)", type_2)))

    cto_vis.add_child(
        TreeNode("Dhaval (Cloud Manager)" if type_2 == 'both' else extract_values("Dhaval (Cloud Manager)", type_2)))
    cto_vis.add_child(
        TreeNode("Abhijit (App Manager)" if type_2 == 'both' else extract_values("Abhijit (App Manager)", type_2)))

    hr_lead.add_child(TreeNode(
        "Peter (Recruitment Manager)" if type_2 == 'both' else extract_values("Peter (Recruitment Manager)", type_2)))
    hr_lead.add_child(
        TreeNode("Waqas (Policy Manager)" if type_2 == 'both' else extract_values("Waqas (Policy Manager)", type_2)))

    root.add_child(cto)
    root.add_child(hr_lead)

    root.print_tree()


if __name__ == "__main__":
    business_model("both")
