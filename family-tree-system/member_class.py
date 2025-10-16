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
