class Patient:

    def __init__(self, ssn, dob, ins_acct_num, first_name, last_name, address):

        self.__ssn = ssn
        self.__dob = dob
        self.__ins_acct_num = ins_acct_num
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__full_name = ""

    @property # ssn getter
    def ssn(self):
        try:
            return self.__ssn
        except AttributeError:
            return "It's wrong"
    
    @property # dob getter
    def dob(self):
        try:
            return self.__dob
        except AttributeError:
            return "No DOB on file"
    
    @property # ins acct number getter
    def ins_acct_num(self):
        try:
            return self.__ins_acct_num
        except AttributeError:
            return "Not on file"

    @property # address getter
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return "Address must be a string"

    @address.setter #setter - duh
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError("Please provide a string value for the address")

    @property # full name getter
    def full_name(self):
        try:
            return self.__first_name + " " + self.__last_name
        except AttributeError:
            return "It's wrong"


    def __str__(self):
        return f"{self.full_name}, {self.dob}, {self.ssn}, {self.__first_name}, {self.__last_name}, {self.address}"