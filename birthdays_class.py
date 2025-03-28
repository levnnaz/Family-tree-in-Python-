
from familytree_database import family_tree
from familytree_class import FamilyTree
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

        #using for loop to iterate through family tree values
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

