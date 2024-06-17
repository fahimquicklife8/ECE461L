class User:
    def __init__(self, userID="", password=""):
        self.__userID = userID
        self.__password = password
    def set_userID(self, userID):
        self.__userID = userID

    def set_password(self, password):
        self.__password = password

    def get_userID(self):
        return self.__userID

    def get_password(self):
        return self.__password

    def get_superUserKey(self):
        return "None"

    # The __init__ method for class User. It initializes the private data attributes, userID and password, to an empty string

    # <Enter your code here to initialize the class and its private data attributes>

    # The following methods set_userID and set_password are mutators for the class's data attributes.

    # <Enter your code here for the mutator functions for the private data attributes >


    # The following methods get_userID and get_password are the accessors for the attributes mentioned above
    # <Enter your code here for the accessor  functions for the private data attributes >


    # Add a method get_superUserKey which is accessor for an attribute called superUserKey. base class does not have this
    # attribute. Hence, simply return text error message "None" from this function
class superUser(User):

    # <Enter your code here to initialize the superUser class, as a subclass of the User superclass. Please remember
    # that while superUser inherits userID and password from User, it has one additional
    # private attribute, superUserKey, which you need to initialize to "Quantumania">

    def __init__(self, userID="", password="", superUserKey="Quantumania"):
        super().__init__(userID, password)
        self.__superUserKey = superUserKey


    # The get_superUserKey method is the accessor for the __superUserKey attribute
    def get_superUserKey(self):
        return self.__superUserKey









