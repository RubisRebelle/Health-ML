import random
from string import punctuation, ascii_letters, digits
from plyer import notification
# before copying the code or something, read this line, " I am not good at naming variables "



#   Over here i created a list of names (just for testing), if you want you can create a list to
names = ["Eric Boi", "Andrew Walter", "John Matt"]

# here we are creating a class which is the program to check the id and name
class check_id_and_name():
    def __init__(self, new_name, id_no):
        self.new_name = new_name
        self.id_no = id_no

    # this is function which will combine the class functions and execute the program
    @staticmethod
    def askmember():
        while True:
            new_member = input("Are you a new member: ").lower()
            if new_member == "yes".lower():
                project_id_and_name = check_id_and_name
                project_id_and_name.new_person_check("Eric")
                project_id_and_name.the_id('123344')
                break

            elif new_member == 'no'.lower():
                print('You can continue')
                break

            else:
                print('sorry, can you try to rephrase it')

    # In this function i have to check is the user having a valid name
    def new_person_check(self):
            # i can also create a database (maybe)  not now
            print("Ok lets create an account for you")
            while True:
                new_name = input("Please enter your first name: ").lower()
                if new_name in names:
                    print(f'There is already a person named {new_name}, maybe try some other name')

                else:
                    print(f"That is a nice name {new_name}")
                    break
