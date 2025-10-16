

# This project was developed by student of the University of Greenwich Nazar Levchuk and Roman Lupuliak.
# This project is a family tree handling system. When the project is run it shows the list
# of options and the user can choose one of the options by entering the number from 1 to 13
# accordingly to the option user wants to choose. (All the options are the feature from the
# coursework).

from familytree_class import FamilyTree
from birthdays_class import Birthdays
from calculations_class import Calculations
from immediate_family_class import ImmediateFamily

#Family tree commented below just to see the names and to choose the person the user wants
# family_tree = {
# #Otto's side (husband)
#     "otto emmersohn": Member("Otto Emmersohn", birth_date="18/12/1985", death_year=None, father="Henry Emmersohn", mother="Helen Emmersohn"),
#     "tracy emmersohn": Member("Tracy Emmersohn", birth_date="15/07/2009", death_year=None, father="Otto Emmersohn", mother="Cornelia Emmersohn"),
#     "james emmersohn": Member("James Emmersohn", birth_date="15/07/2011", death_year=None, father="Otto Emmersohn", mother="Cornelia Emmersohn"),
#     "charley emmersohn": Member("Charley Emmersohn", birth_date="15/07/2007", death_year=None, father="Otto Emmersohn", mother="Cornelia Emmersohn"),
#     "henry emmersohn": Member("Henry Emmersohn", birth_date="08/06/1978", death_year=None, father="Richard Emmersohn", mother="Katrin Emmersohn"),
#     "richard emmersohn": Member("Richard Emmersohn", birth_date="12/07/1925", death_year="2007", father="Diego Emmersohn", mother="Maria Emmersohn"),
#     "diego emmersohn": Member("Diego Emmersohn", birth_date="09/04/1899", death_year="1980", father=None, mother=None),
#     "maria emmersohn": Member("Maria Emmersohn", birth_date="03/01/1904", death_year="1979", father=None, mother=None),
#     "oliver thomas": Member("Oliver Thomas", birth_date="16/08/1901", death_year="1988", father=None, mother=None),
#     "emilia thomas": Member("Emilia Thomas", birth_date="29/05/1906", death_year="1996", father=None, mother=None),
#     "katrin emmersohn": Member("Katrin Emmersohn", birth_date="07/12/1925", death_year="2007", father="Oliver Thomas", mother="Emilia Thomas"),
#     "helen emmersohn": Member("Helen Emmersohn", birth_date="04/03/1960", death_year=None, father="John Balan", mother="Lily Balan"),
#     "john balan": Member("John Balan", birth_date="13/09/1928", death_year="2004", father="Andrei Balan", mother="Elena Balan"),
#     "andrei balan": Member("Andrei Balan", birth_date="30/10/1902", death_year="1991", father=None, mother=None),
#     "elena balan": Member("Elena Balan", birth_date="02/02/1904", death_year="1990", father=None, mother=None),
#     "lily balan": Member("Lily Balan", birth_date="05/08/1930", death_year="2024", father="Bernard Meyer", mother="Lina Meyer"),
#     "bernard meyer": Member("Bernard Meyer", birth_date="22/01/1903", death_year="1989", father=None, mother=None),
#     "lina meyer": Member("Lina Meyer", birth_date="10/10/1907", death_year="1986", father=None, mother=None),
#     "nicole fernandes": Member("Nicole Fernandes", birth_date="24/03/1963", death_year=None, father="John Balan", mother="Lily Balan"),
#     "ahmed fernandes": Member("Ahmed Fernandes", birth_date="01/05/1961", death_year=None, father=None, mother=None),
#     "jerry fernandes": Member("Jerry Fernandes", birth_date="11/12/2019", death_year=None, father="Ahmed Fernandes", mother="Nicole Fernandes"),
#     "ali balan": Member("Ali Balan", birth_date="15/07/1959", death_year="2020", father="John Balan", mother="Lily Balan"),
#     "harry jones": Member("Harry Jones", birth_date="28/02/2013", death_year=None, father="Oliver Jones", mother="Lucy Jones"),
#     "lucy jones": Member("Lucy Jones", birth_date="14/11/1988", death_year=None, father="Henry Emmersohn", mother="Helen Emmersohn"),
#     "oliver jones": Member("Oliver Jones", birth_date="06/09/1983", death_year=None, father=None, mother=None),
#     "cristian rodgers": Member("Cristian Rodgers", birth_date="21/09/1990", death_year=None, father="Paul Rodgers", mother="Angela Rodgers"),
#     "paul rodgers": Member("Paul Rodgers", birth_date="17/02/1959", death_year=None, father=None, mother=None),
#     "angela rodgers": Member("Angela Rodgers", birth_date="26/10/1960", death_year=None, father="Richard Emmersohn", mother="Katrin Emmersohn"),
#     "harry emmersohn": Member("Harry Emmersohn", birth_date="23/03/1923", death_year=None, father="Diego Emmersohn", mother="Maria Emmersohn"),
# #Cornelia side (wife)
#     "cornelia emmersohn": Member("Cornelia Emmersohn", birth_date="21/07/1990", death_year=None, father="Ravi Patel", mother="Priya Gupta"),
#     "andrew emmersohn": Member("Andrew Emmersohn", birth_date="21/07/1990", death_year=None, father=None, mother=None),
#     "james sunak": Member("James Sunak", birth_date="09/11/1992", death_year=None, father="Ashok Sunak", mother="Kavita Singh"),
#     "kavita singh": Member("Kavita Singh", birth_date="04/01/1965", death_year=None, father=None, mother=None),
#     "ashok sunak": Member("Ashok Sunak", birth_date="27/06/1978", death_year=None, father=None, mother=None),
#     "sarah gupta": Member("Sarah Gupta", birth_date="07/07/1995", death_year=None, father="Suresh Gupta", mother="Antoana Gupta"),
#     "suresh gupta": Member("Suresh Gupta", birth_date="03/03/1969", death_year=None, father=None, mother=None),
#     "antoana gupta": Member("Antoana Gupta", birth_date="29/07/1970", death_year=None, father=None, mother=None),
#     "priya gupta": Member("Priya Gupta", birth_date="13/12/1976", death_year=2020, father="Suraj Gupta", mother="Meera Gupta"),
#     "suraj gupta": Member("Suraj Gupta", birth_date="05/03/1920", death_year=1980, father="Rajesh Gupta", mother="Lakshmi Gupta"),
#     "meera gupta": Member("Meera Gupta", birth_date="11/04/1925", death_year=1993, father="Naveen Kumar", mother="Priya Kumar"),
#     "rajesh gupta": Member("Rajesh Gupta", birth_date="01/11/1890", death_year=1950, father=None, mother=None),
#     "lakshmi gupta": Member("Lakshmi Gupta", birth_date="15/07/1900", death_year=1968, father=None, mother=None),
#     "naveen kumar": Member("Naveen Kumar", birth_date="20/02/1902", death_year=1975, father=None, mother=None),
#     "priya kumar": Member("Priya Kumar", birth_date="08/12/1893", death_year=1963, father=None, mother=None),
#     "philip patel": Member("Philip Patel", birth_date="21/06/1927", death_year=2001, father="Yana Shinpilin", mother="Anton Patel"),
#     "anne patek": Member("Anne Patek", birth_date="14/02/1929", death_year=2010, father="Viktor Patek", mother="Elena Patek"),
#     "anton patel": Member("Anton Patel", birth_date="30/05/1906", death_year=1972, father=None, mother=None),
#     "yana shinpilin": Member("Yana Shinpilin", birth_date="19/09/1896", death_year=1965, father=None, mother=None),
#     "viktor patek": Member("Viktor Patek", birth_date="25/08/1892", death_year=1958, father=None, mother=None),
#     "elena patek": Member("Elena Patek", birth_date="13/03/1889", death_year=1947, father=None, mother=None),
#     "ravi patel": Member("Ravi Patel", birth_date="06/09/1965", death_year=None, father="Philip Patel", mother="Anne Patek"),
# }


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
                print(f"Grandchildren for chosen person are: {', '.join(grandchildren)}")
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
