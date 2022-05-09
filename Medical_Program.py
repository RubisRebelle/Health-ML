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


    # This is the official and the main disease program
    @staticmethod
    def disease_program():
        def user_input():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source)

            try:
                search_input = r.recognize_google(audio)
                print("You said: {}".format(search_input))
            except sr.UnknownValueError:
                print("Sorry i could not hear that, :(")
                return None
            return search_input
        driver = webdriver.Chrome()
        driver.get('https://symptoms.webmd.com/')
        driver.maximize_window()
        while True:
            try:
                speak('Can you please tell me what is your age')
                ask_age = user_input()
            except ValueError:
                print('The value you entered is incorrect')
            else:
                break
        age = driver.find_element_by_xpath('//*[@id="age"]')
        age.send_keys(ask_age)
        while True:
            speak('Can you please tell me what is your gender')
            gender = user_input()
            if gender == 'Male'.lower():   #  If your input is being changed to "MAIL" instead of Male then change this Male to Mail 
                male = driver.find_element_by_xpath('//*[@id="male"]')
                male.click()
                break
            elif gender == 'Female'.lower():
                female = driver.find_element_by_xpath('//*[@id="female"]')
                female.click()
                break
            else:
                print('Sorry i did not understand what you wrote ')
        continue_ = driver.find_element_by_xpath('//*[@id="ContentPane30"]/div/div/div/div[2]/div/div/div[2]/button')
        continue_.click()

        # this a function in which we can enter our disease
        def enter_disease():
            speak('Can you please tell me your symptoms')
            ask_symptoms = user_input()
            enter_symptom = driver.find_element_by_xpath('//*[@id="ContentPane30"]/div/div/div/div[3]/div[1]/div[1]/div[2]/input')
            enter_symptom.send_keys(ask_symptoms)
            import pyautogui
            print(pyautogui.position())
            import time
            time.sleep(5)
            pyautogui.click(442, 618)
        enter_disease()
        while True:
            print('Do you want to enter more diseases? : ')
            ask_more = user_input()
            if ask_more == 'Yes'.lower():
                enter_disease()
            elif ask_more == 'No'.lower():
                print('Ok finding the disease related to your symptom')
                break
            else:
                print('Sorry, I cannot understand what you said')

        click_continue = driver.find_element_by_xpath('//*[@id="ContentPane30"]/div/div/div/div[3]/div[2]/button[2]')
        click_continue.click()

        click_continue_2 = driver.find_element_by_xpath('//*[@id="ContentPane30"]/div/div/div/div[3]/div[2]/button[2]')
        click_continue_2.click()
        
        conditions_page = driver.find_element_by_xpath('//*[@id="ContentPane30"]/div/div/div/div[3]/div[2]')
        print(conditions_page.text)

        time.sleep(10)

        return 'nice'

    # Here i am creating a function which rates the app
    def rating_app(self):
        print('Thank you for using this app')
        speak('now you have to rate the app')
        while True:
            rate = float(input('Rating: '))
            if rate > 5:
                print('Sorry you have to rate it out of 5')
            else:
                print('Thank you for your generous rating')
                break
        notification.notify(
            title = 'Meddie',
            message = 'You have successfully closed this up'
        )
        return 'The code worked pretty well'

program = MeddieProgram.program_run()
print(program)
# This is the program :)
