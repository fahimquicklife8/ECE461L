#This is Software Lab HW3 on OOPS
#Name: Fahim Imtiaz
#Professor: Abhay Samant

class hardwareSet:

    def __init__(self):
        self.__Capacity = 0
        self.__Availability = 0

    def initialize_capacity(self, qty):
    #gets quantity of 250 from test file
         self.__Capacity = qty
         self.__Availability = qty

    def get_availability(self):
        #when get method is called avaibility is returned
        return self.__Availability
    def get_capacity(self):
        #when capacity method is called capacity is returned
        return self.__Capacity

    #Main logic is below
    def check_out(self, qty):
        if qty <= self.__Availability:
            self.__Availability = self.__Availability - qty#bug fixed as check_out gets called err != 0 but we return 0 for that
            return 0
        else:
            self.__Availability = 0      #if quantity requested is more then we just set availability to 0
            return -1

    def check_in(self, qty):
        if qty + self.__Availability <= self.__Capacity: #new items checked in plus availability should be less than capacity
            self.__Availability = self.__Availability + qty  #if condition met then checked in item is stored and 0 is returned
            return 0
        else:
            return -1                     #if not just return - 1 since we cannot check in what was never checked out








