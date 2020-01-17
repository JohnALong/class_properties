class Student:
    # set all as empty strings in init
    
    def __init__(self):

        self.__first_name = ""
        self.__last_name = ""
        self.__age = 0
        self.__cohort = 0
        self.__full_name = ""

    @property #getter
    def full_name(self):
        try:
            return self.first_name + " " + self.last_name
        except AttributeError:
            return "It's wrong"
    
    @property # getter
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return ""

    @first_name.setter #setter - duh
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError("Please provide a string value for the first name")

    @property # getter
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return ""

    @last_name.setter #setter - duh
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError("Please provide a string value for the last name")

    @property # getter
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return ""

    @age.setter #setter - duh
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError("Please provide an integer value for age")

    @property # getter
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            return ""

    @cohort.setter #setter - duh
    def cohort(self, new_cohort):
        if type(new_cohort) is int:
            self.__cohort = new_cohort
        else:
            raise TypeError("Please provide an integer value for the Cohort")

    def __str__(self):
        return f"{self.full_name} is {str(self.age)} years old and is in Cohort {self.cohort}"

    