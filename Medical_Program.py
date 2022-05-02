import pyttsx3
import checking_the_id_and_name
import time
from selenium import webdriver
import webbrowser
from plyer import notification
import speech_recognition as sr

# I can also create a text file for storing all the names, ID and all

engine = pyttsx3.init('sapi5')

program_name = 'Meddie'

# here i am creating a function which allows the program to speak for that you have to first install pyttsx3 ( pip install pyttsx3 )
def speak(text):
    engine.say(text)
    engine.runAndWait()


print(checking_the_id_and_name)

# Here i am programming a class which is the main program
class MeddieProgram():
    def __init__(self, ask_disease, *args):
        self.ask_disease = ask_disease

    # here i create a static method which runs all the program
    @staticmethod
    def program_run():
        program_project = MeddieProgram
        program_project.greet_user('greet')
        program_project.create_a_bio('bio')
        program_project.disease_program()
        program_project.rating_app(5)

    # Here i am creating a function which wishes the user according to the time
    def greet_user(self):
        import datetime
        print('Initializing Meddie')
        def wish_user():
            hour = datetime.datetime.now().hourb
            if hour >= 0 and hour <= 12:
                speak('Good Morning')
            elif hour >= 12 and hour <= 18:
                print('Good Afternoon')
            else:
                print('Good Evening')

        time.sleep(5)
        speak(f'Hi am {program_name} and I am your AI doctor ')
        speak('Welcome to the Meddie App')
        return True

    # Over here i am creating a function which is like a quick bio for the app
    def create_a_bio(self):
        bio_name = []
        bio_list = []
        speak('Before starting lets create a quick bio')
        name = input('Enter your name for the bio: ')
        print(bio_name.append(name))
        ask_bio = input('HEY CAN YOU please tell me something about yourself: ')
        print(bio_list.append(ask_bio))
        print('Ok thank you appreciate it ')
        print(list(zip(bio_name, bio_list)))
        write_txt = open("eric_codes.txt","w+")
        write_txt.write(name and ask_bio)
