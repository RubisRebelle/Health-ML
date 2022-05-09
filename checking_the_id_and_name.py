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

    # a function for checking the id of the user
    def the_id(self):
        id_codes = ["eric_go_brr", "i_am_awesome", "dja7623d"]  # id list for testing 'duh'
        while True:
            try:
                ask_id = str(input('Do you want to make your own ID or not, (Yes = make own id, No = let the bot make an ID )): ')).lower()
            except ValueError:
                print('I think the value you entered is incorrect')

            if ask_id == 'Yes'.lower():
                print('Ok now you may enter your id below')
                while True:
                    human_id = input('Please enter a 8 letter ID: ')
                    if len(human_id) > 8:
                        print('YOUR ID CODE SHOULD HAVE 8 CHARACTERS ONLY!!!!!')
                    elif len(human_id) < 8:
                        print('Your id code should at least have 8 characters')
                    else:
                        print('You are good to go')
                        break

                break

            elif ask_id == 'No'.lower():
                print("Okay we can help you make your code")

                def bot_make_id():
                    combined = ascii_letters
                    secure_random = random.SystemRandom()

                    passwords = "".join(secure_random.choice(combined) for i in range(8))
                    print(passwords)

                bot_make_id()

                # this function is to review the bot id
                def review_code():
                    while True:
                        bot_make_id()
                        bot_code = input('Is this code good to go? : ').lower()
                        if bot_code == 'yes':
                            print('Ok, Thank you for the feedback')
                            break

                        elif bot_code == 'no':
                            print('OK the bot will generate another code for you, Please wait')
                            bot_make_id()
                        else:
                            print('Sorry, i cannot understand what you said')

                review_code()
                break

            else:
                print('Sorry, i cannot understand anything')

# Here we execute the program
project_program = check_id_and_name.askmember()
print(project_program)

# Over here i create another function which re checks the id and name (and those who give the input as no "in the begining")
def ask_name_and_id():
    def check_name():
        name = input("What is your full name: ")
        if name in names:
            print('This name is already taken')

        else:
            print(f'Nice name {name}')


    
    #     Over here i  created a function which checks if th users id is valid or not
    def check_id():
        id = str(['hello123', 'ericcode', '1223lf54',]) # here also i created a list of name  for testing
        # and also the user viewing or forking this code follow str = 'Eric Codes' on youtube
        while True:
            get_id = str(input('Your id: '))
            if len(get_id) < 8:
                print('')
            elif len(get_id) > 8:
                print('This id is already taken')
            else:
                print('This is a very nice id')
                break

    # you can also create an account in Twilio to send sms
    # this is a function to send a notification
    def send_notification():
        notification.notify(

            title='Meddie',
            message='You have successfully finished setting up Meddie'

        )
        return 'nice'

    check_name()

    check_id()

    send_notification()

ask_name_and_id()