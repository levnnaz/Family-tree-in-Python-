# This project was developed by student of the University of Greenwich.
# This project is a family tree handling system. When the project is run it shows the list
# of options and the user can choose one of the options by entering the number from 1 to 13
# accordingly to the option user wants to choose. (All the options are the feature from the
# coursework).


#main class Member that takes all the attributes of the instance from family_tree dictionary
class Member:
    def __init__(self, name, birth_date, death_year, father, mother):
        #encapsulating attributes of the instance
        self.__name = name
        self.__birth_date = birth_date
        self.__death_year = death_year
        self.__father = father
        self.__mother = mother
        self.__spouse = []

    #getters and setters methods for the attributes
    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date

    def get_death_year(self):
        return self.__death_year

    def get_father(self):
        return self.__father

    def get_mother(self):
        return self.__mother

    def get_spouse(self):
        return self.__spouse

    #method to add the spouse
    def add_spouse(self,spouse):
        self.__spouse.append(spouse)


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
        return parents #returning parents

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
        #getting member parents
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
        #get member object
        member = family_tree[member_name]
        #get member parents
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

#class Birthdays that inherits from class FamilyTree to get birthdays and sorted calendar
class Birthdays(FamilyTree):
    #method to get birthdays for all member of the family tree
    def get_birthdays(self):
        #for loop to find birthdays and print them
        for member in family_tree.values():
            print(f"{member.get_name()} - Date of birth is: {member.get_birth_date()}")
    #method to sort birthdays by day and month
    def sort_birthdays(self):
        birthdays_calendar = {} #creating dictionary
        # using for loop to iterate through family tree values
        for member in family_tree.values():
            birth_date = member.get_birth_date()
            # splitting birthday by day and month
            split_birthdate = "/".join(birth_date.split('/')[:2])
            member_name = member.get_name()
            #adding split birthdays to a key which is name to the dictionary
            if split_birthdate not in birthdays_calendar:
                birthdays_calendar[split_birthdate] = [member_name]
            else:
                birthdays_calendar[split_birthdate].append(member_name)
        #sorting birthdays
        sorted_birthdays = sorted(
            birthdays_calendar.items(),
            key=lambda item: (int(item[0].split('/')[1]), int(item[0].split('/')[0])))
        #printing sorted birthdays
        for split_birthdate, member_name in sorted_birthdays:
            print(f"{split_birthdate}: {', '.join(member_name)}")

#Class for managing family members
class ImmediateFamily(FamilyTree):

    # Method to retrieve family members
    def get_immediate_family(self):
        member_name = input("Enter the name of the person: ").lower()
        if member_name not in family_tree:  # Check if the record of person exists in the tree
            print(f"No record of {member_name.capitalize()} found")
            return
        member = family_tree[member_name]

        # Retrieve information about parents, siblings, spouse, and children
        parents = self.get_parents(member_name) or []
        siblings = self.get_siblings(member_name) or []
        spouse = member.get_spouse() or []
        children = self.get_children(member_name) or []

        # Display family
        print(f"Immediate family of {member_name.capitalize()}:")
        print(f"Parents: {', '.join(parents) if parents else 'Not available.'}")
        print(f"Siblings: {', '.join(siblings) if siblings else 'No siblings.'}")
        print(f"Spouse: {', '.join(spouse) if spouse else 'No spouse.'}")
        print(f"Children: {', '.join(children) if children else 'No children.'}")

        # Method to retrieve extended family
    def get_extended_family(self, member_name):
        # Convert the input name to lowercase for consistent dictionary lookup
        member_name = member_name.lower()
        # Check if the person exists in the family tree
        if member_name not in family_tree:
            print(f"No record of {member_name.capitalize()} found")
            return
        member = family_tree[member_name]
        # Get parents and filter for living ones
        parents = [
            p for p in (self.get_parents(member_name) or [])
            if p and family_tree[p.lower()].get_death_year() is None]
        # Siblings and filter for living ones
        siblings = [
            s for s in (self.get_siblings(member_name) or [])
            if s and family_tree[s.lower()].get_death_year() is None]
        # Get spouse(s) and filter for living ones
        spouse = [
            sp for sp in (member.get_spouse() or [])
            if sp and family_tree[sp.lower()].get_death_year() is None]
        # Get children and filter for living ones
        children = [
            c for c in (self.get_children(member_name) or [])
            if c and family_tree[c.lower()].get_death_year() is None]
        # Find aunts and uncles and filter for living ones
        aunts_uncles = set()
        for parent in parents:
            aunts_uncles.update([
                s for s in self.get_siblings(parent.lower())
                if s.lower() != member_name and family_tree[s.lower()].get_death_year() is None])
        # Find cousins (children of the aunts and uncles) and filter for living ones
        cousins = set()
        for aunt_uncle in aunts_uncles:
            cousins.update([
                c for c in (self.get_children(aunt_uncle.lower()) or [])
                if family_tree[c.lower()].get_death_year() is None])
        # Organize the results for display
        family = {
            'Parents': sorted(parents),
            'Siblings': sorted(siblings),
            'Spouse': sorted(spouse),
            'Children': sorted(children),
            'Aunts/Uncles': sorted(aunts_uncles),
            'Cousins': sorted(cousins)}
        # Print the results
        print(f"Extended family of {member_name.capitalize()} (living only):")
        for relation, members in family.items():
            print(f"{relation}: {', '.join(m.capitalize() for m in members) if members else 'None'}")

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
                count_members += 1 #couting dead members1
        #calculating the average age at death
        if count_members > 0:
            average_death_age = int(total_age / count_members)
            return average_death_age #return average at death

    # Method to count the number of children for a family member
    def get_children_count(self):
        member_name = input("Enter the name of person from family tree: ").lower()  # Ask for the name
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
        print(f"The average number of children per person is: {average:.0f}")

#dictionary to store all the member of the Family Tree with the name as a key
family_tree = {
#Otto's side (husband) (Nazar)
    "otto emmersohn": Member("Otto Emmersohn", birth_date="18/12/1985", death_year=None, father="Henry Emmersohn", mother = "Helen Emmersohn"),
    "tracy emmersohn": Member("Tracy Emmersohn", birth_date="15/07/2009", death_year=None, father="Otto Emmersohn", mother="Cornelia Emmersohn"),
    "james emmersohn": Member("James Emmersohn", birth_date="15/07/2011", death_year=None, father="Otto Emmersohn", mother="Cornelia Emmersohn"),
    "charley emmersohn": Member("Charley Emmersohn", birth_date="15/07/2007", death_year=None, father="Otto Emmersohn", mother="Cornelia Emmersohn"),
    "henry emmersohn": Member("Henry Emmersohn", birth_date="08/06/1978", death_year=None, father="Richard Emmersohn", mother="Katrin Emmersohn"),
    "richard emmersohn": Member("Richard Emmersohn", birth_date="12/07/1925", death_year="2007", father="Diego Emmersohn", mother="Maria Emmersohn"),
    "diego emmersohn": Member("Diego Emmersohn", birth_date="09/04/1899", death_year="1980", father=None, mother=None),
    "maria emmersohn": Member("Maria Emmersohn", birth_date="03/01/1904", death_year="1979", father=None, mother=None),
    "oliver thomas": Member("Oliver Thomas", birth_date="16/08/1901", death_year="1988", father=None, mother=None),
    "emilia thomas": Member("Emilia Thomas", birth_date="29/05/1906", death_year="1996", father=None, mother=None),
    "katrin emmersohn": Member("Katrin Emmersohn", birth_date="07/12/1925", death_year="2007", father="Oliver Thomas", mother="Emilia Thomas"),
    "helen emmersohn": Member("Helen Emmersohn", birth_date="04/03/1960", death_year=None, father="John Balan", mother="Lily Balan"),
    "john balan": Member("John Balan", birth_date="13/09/1928", death_year="2004", father="Andrei Balan", mother="Elena Balan"),
    "andrei balan": Member("Andrei Balan", birth_date="30/10/1902", death_year="1991", father=None, mother=None),
    "elena balan": Member("Elena Balan", birth_date="02/02/1904", death_year="1990", father=None, mother=None),
    "lily balan": Member("Lily Balan", birth_date="05/08/1930", death_year="2024", father="Bernard Meyer", mother="Lina Meyer"),
    "bernard meyer": Member("Bernard Meyer", birth_date="22/01/1903", death_year="1989", father=None, mother=None),
    "lina meyer": Member("Lina Meyer", birth_date="10/10/1907", death_year="1986", father=None, mother=None),
    "nicole fernandes": Member("Nicole Fernandes", birth_date="24/03/1963", death_year=None, father="John Balan", mother="Lily Balan"),
    "ahmed fernandes": Member("Ahmed Fernandes", birth_date="01/05/1961", death_year=None, father=None, mother=None),
    "jerry fernandes": Member("Jerry Fernandes", birth_date="11/12/2019", death_year=None, father="Ahmed Fernandes", mother="Nicole Fernandes"),
    "ali balan": Member("Ali Balan", birth_date="15/07/1959", death_year="2020", father="John Balan", mother="Lily Balan"),
    "harry jones": Member("Harry Jones", birth_date="28/02/2013", death_year=None, father="Oliver Jones", mother="Lucy Jones"),
    "lucy jones": Member("Lucy Jones", birth_date="14/11/1988", death_year=None, father="Henry Emmersohn", mother="Helen Emmersohn"),
    "oliver jones": Member("Oliver Jones", birth_date="06/09/1983", death_year=None, father=None, mother=None),
    "cristian rodgers": Member("Cristian Rodgers", birth_date="21/09/1990", death_year=None, father="Paul Rodgers", mother="Angela Rodgers"),
    "paul rodgers": Member("Paul Rodgers", birth_date="17/02/1959", death_year=None, father=None, mother=None),
    "angela rodgers": Member("Angela Rodgers", birth_date="26/10/1960", death_year=None, father="Richard Emmersohn", mother="Katrin Emmersohn"),
    "harry emmersohn": Member("Harry Emmersohn", birth_date="23/03/1923", death_year=None, father="Diego Emmersohn", mother="Maria Emmersohn"),
#Cornelia side (wife) (Roman)
    "cornelia emmersohn": Member("Cornelia Emmersohn", birth_date="21/07/1990", death_year=None, father="Ravi Patel", mother="Priya Gupta"),
    "andrew emmersohn": Member("Andrew Emmersohn", birth_date="21/07/1990", death_year=None, father=None, mother=None),
    "james sunak": Member("James Sunak", birth_date="09/11/1992", death_year=None, father="Ashok Sunak", mother="Kavita Singh"),
    "kavita singh": Member("Kavita Singh", birth_date="04/01/1965", death_year=None, father=None, mother=None),
    "ashok sunak": Member("Ashok Sunak", birth_date="27/06/1978", death_year=None, father=None, mother=None),
    "sarah gupta": Member("Sarah Gupta", birth_date="07/07/1995", death_year=None, father="Suresh Gupta", mother="Antoana Gupta"),
    "suresh gupta": Member("Suresh Gupta", birth_date="03/03/1969", death_year=None, father=None, mother=None),
    "antoana gupta": Member("Antoana Gupta", birth_date="29/07/1970", death_year=None, father=None, mother=None),
    "priya gupta": Member("Priya Gupta", birth_date="13/12/1976", death_year=2020, father="Suraj Gupta", mother="Meera Gupta"),
    "suraj gupta": Member("Suraj Gupta", birth_date="05/03/1920", death_year=1980, father="Rajesh Gupta", mother="Lakshmi Gupta"),
    "meera gupta": Member("Meera Gupta", birth_date="11/04/1925", death_year=1993, father="Naveen Kumar", mother="Priya Kumar"),
    "rajesh gupta": Member("Rajesh Gupta", birth_date="01/11/1890", death_year=1950, father=None, mother=None),
    "lakshmi gupta": Member("Lakshmi Gupta", birth_date="15/07/1900", death_year=1968, father=None, mother=None),
    "naveen kumar": Member("Naveen Kumar", birth_date="20/02/1902", death_year=1975, father=None, mother=None),
    "priya kumar": Member("Priya Kumar", birth_date="08/12/1893", death_year=1963, father=None, mother=None),
    "philip patel": Member("Philip Patel", birth_date="21/06/1927", death_year=2001, father="Yana Shinpilin", mother="Anton Patel"),
    "anne patek": Member("Anne Patek", birth_date="14/02/1929", death_year=2010, father="Viktor Patek", mother="Elena Patek"),
    "anton patel": Member("Anton Patel", birth_date="30/05/1906", death_year=1972, father=None, mother=None),
    "yana shinpilin": Member("Yana Shinpilin", birth_date="19/09/1896", death_year=1965, father=None, mother=None),
    "viktor patek": Member("Viktor Patek", birth_date="25/08/1892", death_year=1958, father=None, mother=None),
    "elena patek": Member("Elena Patek", birth_date="13/03/1889", death_year=1947, father=None, mother=None),
    "ravi patel": Member("Ravi Patel", birth_date="06/09/1965", death_year=None, father="Philip Patel", mother="Anne Patek"),
}

#Assigning spouses
#Otto side spouses
family_tree["cornelia emmersohn"].add_spouse("otto emmersohn")
family_tree["richard emmersohn"].add_spouse("katrin emmersohn")
family_tree["katrin emmersohn"].add_spouse("richard emmersohn")
family_tree["diego emmersohn"].add_spouse("maria emmersohn")
family_tree["maria emmersohn"].add_spouse("diego emmersohn")
family_tree["angela rodgers"].add_spouse("paul rodgers")
family_tree["paul rodgers"].add_spouse("angela rodgers")
family_tree["oliver thomas"].add_spouse("emilia thomas")
family_tree["emilia thomas"].add_spouse("oliver thomas")
family_tree["henry emmersohn"].add_spouse("helen emmersohn")
family_tree["helen emmersohn"].add_spouse("henry emmersohn")
family_tree["john balan"].add_spouse("lily balan")
family_tree["lily balan"].add_spouse("john balan")
family_tree["andrei balan"].add_spouse("elena balan")
family_tree["bernard meyer"].add_spouse("lina meyer")
family_tree["lina meyer"].add_spouse("bernard meyer")
family_tree["lucy jones"].add_spouse("oliver jones")
family_tree["oliver jones"].add_spouse("lucy jones")
family_tree["nicole fernandes"].add_spouse("ahmed fernandes")
family_tree["ahmed fernandes"].add_spouse("nicole fernandes")
#Cornelia side spouses
family_tree["otto emmersohn"].add_spouse("cornelia emmersohn")
family_tree["kavita singh"].add_spouse("ashok sunak")
family_tree["ashok sunak"].add_spouse("kavita singh")
family_tree["suresh gupta"].add_spouse("antoana gupta")
family_tree["antoana gupta"].add_spouse("suresh gupta")
family_tree["priya gupta"].add_spouse("ravi patel")
family_tree["ravi patel"].add_spouse("priya gupta")
family_tree["suraj gupta"].add_spouse("meera gupta")
family_tree["meera gupta"].add_spouse("suraj gupta")
family_tree["rajesh gupta"].add_spouse("lakshmi gupta")
family_tree["lakshmi gupta"].add_spouse("rajesh gupta")
family_tree["naveen kumar"].add_spouse("priya kumar")
family_tree["priya kumar"].add_spouse("naveen kumar")
family_tree["philip patel"].add_spouse("yana shinpilin")
family_tree["yana shinpilin"].add_spouse("philip patel")
family_tree["anne patek"].add_spouse("anton patel")
family_tree["anton patel"].add_spouse("anne patek")
family_tree["viktor patek"].add_spouse("elena patek")
family_tree["elena patek"].add_spouse("viktor patek")
family_tree["ravi patel"].add_spouse("anne patek")
family_tree["anne patek"].add_spouse("ravi patel")

#creating function to call all the methods
def main():
    #printing the options
    print( "1. Print parents of the person in family tree" "\n"
           "2. Print children of the person in family tree" "\n"
           "3. Print spouse of the person in family tree""\n"
           "4. Print siblings of the person in family tree""\n"
           "5. Print cousins of the person in family tree""\n"
           "6. Print birthdays of all members in family tree""\n"
           "7. Print sorted birthdays by day and month of family tree member""\n"
           "8. Print grandchildren for the person in family tree""\n"
           "9. Print immediate family of the person in family tree""\n"
           "10. Print extended family of the person in family tree""\n"
           "11. Print an average age at death in family tree""\n"
           "12. Print the number of children of the person in family tree""\n"
           "13. Print the average number of children in family tree""\n")
#if-elif to print the chosen option from the list
    try:
        option = int(input("Choose the option from the list above (1-13): ")) #input option
        if option == 1:
            member_name = input("Enter the name of the person from family tree: ") #input member name
            o1 = FamilyTree(None, None, None, None, None)
            parents = o1.get_parents(member_name)
            if parents:
                print(f"Parents for {member_name.capitalize()} are: {', '.join(parents)}")
            else:
                print(f"No parents for {member_name.capitalize()} are found")
        elif option == 2:
            member_name = input("Enter the name of the person from family tree: ")
            o2 = FamilyTree(None, None, None, None, None)
            children = o2.get_children(member_name)
            if children:
                print(f"Children for {member_name.capitalize()} are: {', '.join(children)}")
            else:
                print(f"No children for {member_name.capitalize()} are found")
        elif option == 3:
            member_name = input("Enter the name of the person from family tree: ")
            o3 = FamilyTree(None, None, None, None, None)
            spouse = o3.display_spouse(member_name)
            if spouse:
                print(f"Spouse for {member_name.capitalize()} is: {', '.join(spouse)}")
            else:
                print(f"No spouse for {member_name.capitalize()} is found")
        elif option == 4:
            member_name = input("Enter the name of the person from family tree: ")
            o4 = FamilyTree(None, None, None,None, None)
            siblings = o4.get_siblings(member_name)
            if siblings:
                print(f"Siblings for {member_name.capitalize()} are: {', '.join(siblings)}")
            else:
                print(f"No siblings for {member_name.capitalize()} are found")
        elif option == 5:
            member_name = input("Enter the name of the person from family tree: ")
            o5 = FamilyTree(None, None, None, None, None)
            cousins = o5.get_cousins(member_name)
            if cousins:
                print(f"Cousins for {member_name.capitalize()} are: {', '.join(cousins)}")
            else:
                print(f"No cousins for {member_name.capitalize()} are found")
        elif option == 6:
            o6 = Birthdays(None, None, None, None, None)
            o6.get_birthdays()
        elif option == 7:
            o7 = Birthdays(None, None, None, None, None)
            o7.sort_birthdays()
        elif option == 8:
            member_name = input("Enter the name of the person from family tree: ")
            o8 = FamilyTree(None, None, None, None, None)
            grandchildren = o8.get_grandchildren(member_name)
            if grandchildren:
                print(f"Cousins for chosen person are: {', '.join(grandchildren)}")
            else:
                print(f"No grandchildren for {member_name.capitalize()} are found")
        elif option == 9:
            o9 = ImmediateFamily(None, None, None, None, None)
            o9.get_immediate_family()
        elif option == 10:
            member_name = input("Enter the name of the person from family tree: ")
            o10 = ImmediateFamily(None, None, None, None, None)
            o10.get_extended_family(member_name)
        elif option == 11:
            o11 = Calculations(None, None, None, None, None)
            print(f"Average age at death in family tree is: {o11.average_age_at_death()} years old")
        elif option == 12:
            o12 = Calculations(None, None, None, None, None)
            o12.get_children_count()
        elif option == 13:
            o13 = Calculations(None, None, None, None, None)
            o13.average_children_per_person()
        else:
            print('\n' "Choose a valid option from the list (1-13).")
            main()
    except ValueError:
        print("Error. Choose a valid option from the list (1-13).")
        main()
main() #calling the function main




