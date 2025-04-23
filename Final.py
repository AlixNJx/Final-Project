import json
import datetime
import random
import os
import re


def valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return False

    return True

def calc_age(birthYear):
    theYear = datetime.datetime.now().year
    age = theYear - birthYear
    if age < 18:
        return False
    if age > 50:
        return False
    else :
        return True

class register:
    def __init__(self):
        self.username, self.email, self.password, self.birthYear, self.sq1, self.sq2 = self.getdata()

    def load(self):
        with open('db.json', 'r') as file:
            db = json.load(file)
        return db

    def getdata(self):
        db = self.load()
        username = input('Enter your username :').lower()
        i = 0
        while i < len(db):
            if db[i]['Username '] == username:
                print('Username must be unique, please try again ‼️')
                print('-----' * 10)
                username = input('Enter your username :').lower()
                i = -1
            i += 1
        email = input('Enter your Email :').lower()
        while '@gmail.com' not in email and '@yahoo.com' not in email:
            print('Your email address should ends with @gmail.com or @yahoo.com ‼️')
            print('-----' * 10)
            email = input('Enter your Email :').lower()

        while True:
            password = input("Enter Your Password :")
            if valid_password(password):
                break
            else:
                print('Invalid Password.‼️')
                print('-----' * 10)

        while True :
            try:
                birthYear = int(input('Enter your BirthYear :'))
                if calc_age(birthYear):
                    break
                else:
                    print('Invalid Age ‼️')
                    print('-----' * 10)
            except ValueError:
                print('Only Number')
                print('-----' * 10)

        while True:
            sq1 = input('Where were you born ? :').lower()
            if sq1 == 'iran':
                break
            else:
                print('Invalid Answer‼️')
                print('-----' * 10)

        while True:
            sq2 = input('What is 4*5 ? :').lower()
            if sq2 == '20':
                break
            else:
                print('Invalid Answer‼️')
                print('-----' * 10)

        print('-----' * 10)
        print('Registration was successful ✅')
        return username, email, password, birthYear, sq1, sq2

    def write(self):
        db = self.load()
        info = {
            'Username ': self.username,
            'Email ': self.email,
            'Password ': self.password,
            'BirthYear ': self.birthYear,
            'Security Question 1 ': self.sq1,
            'Security Question 2 ': self.sq2,
            'Register Time ': str(datetime.datetime.now()),
        }
        db.append(info)
        with open('db.json', 'w') as file:
            json.dump(db, file, indent=4)

class Login :
    def __init__(self):
        self.username, self.password = self.login()

    def load(self):
        with open('db.json', 'r') as file:
            db = json.load(file)
        return db

    def login(self):
        db = self.load()
        username = input('Enter your username :')
        password = input('Enter your password :')
        flag = False
        for i in db :
            if i.get('Username ') == username and i.get('Password ') == password:
                print('Welcome To Your Profile ✅')
                print('-----' * 10)
                register_course()
                return username, password
        print('Your username or password was wrong, please try again ‼️')
        print('-----' * 10)
        return None, None

class register_course :
    def __init__(self):
        self.choose_course = self.choose_course()

    def load(self):
        with open('db.json', 'r') as file:
            db = json.load(file)
        return db

    def choose_course(self):
        db = self.load()
        while True :
            choosing = input('Choose the option :\n1)Language Course\n2)Exam\n3)Exit\n -->')
            if choosing == '1' :
                LanguageCourse()
            elif choosing == '2' :
                quiz.start()
            elif choosing == '3' :
                print('Ok, See you later ✅')
                print('-----' * 10)
                break
            else :
                print('Invalid Answer ‼️')
                print('-----' * 10)

class LanguageCourse :
    def __init__(self):
        self.username = self.get_name()
        self.course = self.course()

    def load(self):
        with open('course.json', 'r') as file:
            db = json.load(file)
        return db

    def get_name(self):
        first_name = input('Enter your first name :')
        last_name = input('Enter your last name :')
        self.username = f'{first_name} {last_name}'
        return self.username

    def course(self):
        db = self.load()
        while True :
            course = input('What course do you want to attend :\n1)English Course\n2)Spanish Course\n3)Deutsch Course\n4)Russian Course\n5)Exit\n--> ')
            if course == '1' :
                print('The English course was successfully registered ✅')
                print('-----' * 10)
                self.course = 'English'
                self.course_writer()
            elif course == '2' :
                print('The Spanish course was successfully registered ✅')
                print('-----' * 10)
                self.course = 'Spanish'
                self.course_writer()
            elif course == '3' :
                print('The Deutsch course was successfully registered ✅')
                print('-----' * 10)
                self.course = 'Deutsch'
                self.course_writer()
            elif course == '4' :
                print('The Russian course was successfully registered ✅')
                print('-----' * 10)
                self.course = 'Russian'
                self.course_writer()
            elif course == '5' :
                print('Ok, until we meet again ✅')
                print('-----' * 10)
                break
            else:
                print('Invalid Answer, Please try again ‼️')
                print('-----' * 10)
                continue

    def course_writer(self):
        db = self.load()
        data = {
            'Username ' : self.username,
            'Course ' : self.course,
            'Registration Time ' : str(datetime.datetime.now()),
        }
        db.append(data)
        with open('course.json', 'w') as file :
            json.dump(db, file, indent=4)

class Exam :
    def __init__(self):
        self.name = ''
        self.score = 0
        self.question = [
            {
                'question ' : '🔺where is the capital of france?🔺',
                'option ' : ['1)europe','2)italy','3)paris','4)none'],
                'answer ' : 3
            },{
                'question ' : '🔺how many continent do we have ?🔺 ',
                'option ' : ['1)5','2)6','3)7','4)8'],
                'answer ' : 4
            },{
                'question ' : '🔺what is the official language of iran? 🔺',
                'option ' : ['1)arabic','2)farsi','3)french','4)turkish'],
                'answer '  : 2
            },{
                'question ' : '🔺where is the capital of italy?🔺 ',
                'option ' : ['1)vanice','2)florance','3)milan','4)rome'],
                'answer ' : 4
            },{
                'question ' : '🔺how many fingers do we have ?🔺',
                'option ' :  ['1)5','2)3','3)8','4)4'],
                'answer ' : 1
            }
        ]

    def load(self):
        with open('score.json', 'r') as file:
            db = json.load(file)
        return db

    def start(self):
        self.get_name()
        self.run_quiz()

    def get_name(self):
        self.name = input('Enter your firstname & lastname :')

    def run_quiz(self):
        for idx, q in enumerate(self.question) :
            print(f'{idx + 1}: {q['question ']}')
            for opt in q['option ']:
                print(opt)
            try :
                user_answer = int(input('Enter an option between 1 and 4 :'))
                if user_answer == q['answer '] :
                    self.score += 1
            except ValueError :
                print('Invalid Answer ‼️')
                print('-----' * 10)
        print('End of Quiz ✅')
        print('-----' * 10)
        print(f'Dear {self.name} your score is : {self.score} out of 5 ✅')
        print('-----' * 10)
        self.save_score()

    def save_score(self):
        db = self.load()
        data = {
            'Username ' : self.name,
            'Score ' : self.score,
            'Quiz Time ' : str(datetime.datetime.now())
        }

        db.append(data)

        with open('score.json', 'w') as file :
            json.dump(db, file, indent=4)

quiz = Exam()

class forgot_password :
    def __init__(self):
        self.forgot_password = self.forgot_password()

    def load(self):
        with open('db.json', 'r') as file:
            db = json.load(file)
        return db

    def write2json(self, db):
        with open('db.json', 'w') as file:
            json.dump(db, file, indent=4)

    def forgot_password(self):
        db = self.load()
        username = input('Enter your username :')
        sq1 = input('Where were your born ? :')
        sq2 = input('What is 4*5 ? :')
        flag = False
        for user in db :
            if user['Username '] == username and sq1 == 'iran' and sq2 == '20':
                print('Now you can enter your new password ✅')
                print('-----' * 10)
                new_password = input('Enter your new password :')
                user['Password '] = new_password
                self.write2json(db)
                print('Password Changed ✅')
                print('-----' * 10)
                flag = True
                return username, sq1, sq2, new_password
        if not flag :
            print('Username not found or Security answers incorrect')
            print('---' * 10)

class main :
    def __init__(self):
        self.menu = main

    def load(self):
        with open('db.json', 'r') as file:
            db = json.load(file)
        return db

    def main(self):
        db = self.load()
        while True:
            menu = input('Choose Your Option : \n1)Sign Up\n2)Log In\n3)Forgot Password\n4)Exit\n --> ')
            if menu == '1':
                register().write()
            elif menu == '2':
                Login()
            elif menu == '3':
                forgot_password()
            elif menu == '4':
                print('Thanks for using our system ✅')
                print('-----' * 10)
                break
            else:
                print('Invalid Answer ‼️')
                print('-----' * 10)

main = main()
main.main()
