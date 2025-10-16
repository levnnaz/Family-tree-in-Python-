
from familytree_database import family_tree
from familytree_class import FamilyTree
#Class to calculate the age, children etc. from family tree
class Calculations(FamilyTree):
    #method to calculate average age at death in the family tree
    def average_age_at_death(self):
        #variable for counting
        total_age = 0
        count_members = 0
        #for loop to find the age at death for all members
        for member in family_tree.values():
            #cheking if member is not alive
            if member.get_death_year() is not None:
                birth_year = int(member.get_birth_date().split("/")[2])
                death_year = int(member.get_death_year())
                total_age += (death_year - birth_year)
                count_members += 1 #couting dead members
        #calculating the average age at death
        if count_members > 0:
            average_death_age = int(total_age / count_members)
            return average_death_age #return average at death

    # Method to count the number of children for a family member
    def get_children_count(self):
        member_name = input("Enter the ame of person from family tree: ").lower()  # Ask for the name
        member = family_tree.get(member_name)  # Retrieve the family member

        if not member:  # If the name doesn't exist
            print(f"No record of {member_name.capitalize()} found")
            return

        # Count the number of children through either parent
        children_count = 0
        for child in family_tree.values():
            if child.get_father() and child.get_father().lower() == member_name.lower():
                children_count += 1
            elif child.get_mother() and child.get_mother().lower() == member_name.lower():
                children_count += 1

        # Print the result
        print(f"{member_name.capitalize()} has {children_count} children.")

     # Method to calculate the average number of children per person
    def average_children_per_person(self):
        total_people = len(family_tree)  # Total number of people
        # Calculate the total number of children
        total_children = sum(len([
                child for child in family_tree.values()
                if (child.get_father() and child.get_father().lower() == person.get_name().lower()) or
                    (child.get_mother() and child.get_mother().lower() == person.get_name().lower())])
            for person in family_tree.values())
        # Calculate the average
        average = total_children / total_people if total_people > 0 else 0
        print(f"The average number of children per person is: {average:.0f}") #print average age
