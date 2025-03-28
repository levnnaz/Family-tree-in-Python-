
from member_class import Member
from familytree_database import family_tree
# Creating the class FamilyTree that inherits from class Member to find the relationships
class FamilyTree(Member):
    def __init__(self, name, birth_date, death_year, father, mother):
        super().__init__(name, birth_date, death_year, father, mother)

    # method to get children for the person from family tree
    def get_children(self, member_name):
        children = [] #creating a list
        member_name = member_name.lower()
        # checking if member_name is in family tree
        if member_name not in family_tree:
            print(f"No record of {member_name.capitalize()} found")
            return
        #using for loop and if to find the children from the family tree values
        for child in family_tree.values():
            #cheking in the values if parents of the persons are equal to member
            if (child.get_father() and member_name == child.get_father().lower()
            or child.get_mother() and member_name == child.get_mother().lower()):
                children.append(child.get_name()) #append child in the list if found
        return children #return list of children

    # creating method get_parents to display parent of the person from family tree
    def get_parents(self, member_name):
        parents = []
        member_name = member_name.lower()
        # checking if member_name is in family tree
        if member_name not in family_tree:
            print(f"No record of {member_name.capitalize()} found")
            return
        # assigning to member the key from the family_tree
        member = family_tree[member_name]
        # checking if there are parents for the member
        if member.get_father() is not None:
            # assigning member's father and mother to the variables accordingly and adding to the list
            father = member.get_father()
            parents.append(father)
        if member.get_mother() is not None:
            mother = member.get_mother()
            parents.append(mother)
        return parents  # returning parents

    # method to display the spouse
    def display_spouse(self, member_name):
        member_name = member_name.lower()
        #checking if member_name is in family tree
        if member_name not in family_tree:
            print(f"No record of {member_name.capitalize()} found")
            return
        member = family_tree[member_name] #assigning the key from family_tree to the variable member
        return member.get_spouse() #return spouse of the member

    #method to find siblings of the person from family tree
    def get_siblings(self, member_name):
        siblings = []  # List for siblings
        member_name = member_name.lower()
        # Check if the member_name is in family tree
        if member_name not in family_tree:
            print(f"No record of {member_name.capitalize()} found")
            return
        member = family_tree[member_name]  # Get the member object
        # getting member parents
        member_father = member.get_father()
        member_mother = member.get_mother()
        # Check all members in the family tree for potential siblings
        for sibling in family_tree.values():
            if sibling == member:
                continue
            # Checking for one of the parents
            if (member_father is not None and sibling.get_father() == member_father
            or member_mother is not None and sibling.get_mother() == member_mother):
                siblings.append(sibling.get_name())  # Add sibling's name to the list

        return siblings  # Return the list of siblings

    #method to find cousins of the person
    def get_cousins(self, member_name):
        # Create lists for cousins and parents' siblings
        cousins = []
        parents_siblings = []
        member_name = member_name.lower()
        # Check if the member_name is in family tree
        if member_name not in family_tree:
            print(f"No record of {member_name.capitalize()} found")
            return
        # get member object
        member = family_tree[member_name]
        # get member parents
        member_father = member.get_father()
        member_mother = member.get_mother()
        # Check if the member has one of the parents
        if member_father is not None:
            # Add father's siblings to the parents_siblings list
            parents_siblings.extend(self.get_siblings(member_father.lower()))
        if member_mother is not None:
            # Add mother's siblings to the parents_siblings list
            parents_siblings.extend(self.get_siblings(member_mother.lower()))
        for cousin in family_tree.values():
            # Check if cousin's parents are in the parents_siblings list
            if cousin.get_father() in parents_siblings or cousin.get_mother() in parents_siblings:
                cousins.append(cousin.get_name())
        return cousins  # Return the list of cousins

    # Method to get the grandchildren of a family member
    def get_grandchildren(self, member_name):
        member_name = member_name.lower()  # Convert the name to lowercase
        # Check if the family member exists in the tree
        if member_name not in family_tree:
            print(f"No record of {member_name.capitalize()} found")  # Message if the member is not found
            return
        children = self.get_children(member_name)  # Retrieve the children
        grandchildren = []
        # For each child, retrieve their children (grandchildren)
        for child in children:
            grandchildren += self.get_children(child.lower())
        return grandchildren  # Return the list of grandchildren
