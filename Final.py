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

# class CheckAnswer :
#     def __init__(self):
#         self.questions = questions
#         self.options = options
#         self.correct_answer = correct_answer
#         self.scores = {}
#         self.answer = {}
#
#     def load(self):
#         with open('score.json', 'r') as file :
#             db = json.load(file)
#         return db
#
#     # def write2json(self):
#     #     with open('db.json', 'w') as file :
#     #         json.dump(db, file, indent=4)
#
#     def check_answer(self):
#         return user_answer == self.correct_answer
#
#     def quiz(self):
#         self.questions = questions
#         self.user_score = 0
#
#         for idx, question in enumerate(self.questions, 1) :
#             print(f'{idx} : {question['Questions']}')
#             for option in question['Option'] :
#                 print(option)
#             user_answer = input('What is your answer :')
#             if user_answer.lower() == question['answer'].lower():
#                 self.user_score += 1
#                 print('Your answer wae correct ✅')
#                 print('-----' * 10)
#             else :
#                 print('Your answer war wrong ‼️')
#                 print('-----' * 10)
#     def end_quiz(self):
#         print(f'Your total score is : {self.user_score}')
#         print('-----' * 10)
#
#     def save_score(self):
#         with open('score.json') as file :
#             json.dump('score.json', file, indent=4)
#         print('Saved ✅')
#         print('-----' * 10)
#
#     def scores(self):
#         try :
#             with open('score.json', 'r') as file :
#                 self.user_score = json.load(file)
#                 print('Saved ✅')
#                 print('-----' * 10)
#         except FileNotFoundError:
#             print('Error ‼️')

# class Question:
#     def __init__(self,question_text,options,correct_answer):
#         self.question_text = question_text
#         self.options = options
#         self.correct_answer = correct_answer
#
#     def load(self):
#         with open('score.json', 'r') as file:
#             db = json.load(file)
#             return db
#
#     def check_answer(self,answer):
#         return answer == self.correct_answer

# class Exam :
#     def __init__(self):
#         self.username = self.get_name()
#         self.exam = self.exam()
#         self.user_score = self.user_score()
#
#     def load(self):
#         with open('score.json', 'r') as file :
#             db = json.load(file)
#         return db
#
#     def get_name(self):
#         first_name = input('Enter your first name :')
#         last_name = input('Enter your last name :')
#         self.username = f'{first_name} {last_name}'
#         return self.username
#
#     def exam(self):
#         db = self.load()
#         user_score = 0
#         while True :
#             question1 = input('Where is the capital of france ?\n1)europe\n2)italy\n3)paris\n4)none\n -->')
#             if  question1 == '3' :
#                 print('Correct')
#                 user_score += 1
#             else :
#                 print('Wrong')
#             question2 = input('How many continent do we have ?\n1)5\n2)6\n3)7\n4)8\n -->')
#             if question2 == '8' :
#                 print('Correct')
#                 user_score += 1
#             else :
#                 print('Wrong')
#             question3 = input('What is the official language of iran ?\n1)arabic\n2)persian\n3)french\n4)turkish\n -->')
#             if question3 == '2' :
#                 print('Correct')
#                 user_score += 1
#             else :
#                 print('Wrong')
#             question4 = input('Where is the capital of italy ?\n1)napoli\n2)florance\n3)milan\n4)rome\n -->')
#             if question4 == '4' :
#                 print('Correct')
#                 user_score += 1
#             else :
#                 print('Wrong')
#             question5 = input('How many fingers do we have ?\n1)5\n2)3\n3)8\n4)4\n -->')
#             if question5 == '1' :
#                 print('Correct')
#                 user_score += 1
#             else :
#                 print('Wrong')
#                 break
#
#     def writeScore(self):
#         db = self.load()
#         result = {
#             'Username ' : self.username,
#             'User Score ' : self.user_score,
#         }
#         db.append(result)
#
#         with open('score.json', 'w') as file :
#             json.dump(db, file, indent=4)
#             print('Saved')

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

        # filename = 'score.json'
        # scores = []

        # with open('score.json', 'r') as file :
        #     try :
        #         scores = json.load(file)
        #     except json.JSONDecoderError :
        #         scores = []

        db.append(data)

        with open('score.json', 'w') as file :
            json.dump(db, file, indent=4)

quiz = Exam()

# quiz.username()
# quiz.run_quiz()

# class Exam:
#     def __init__(self):
#         self.username = self.get_name()
#         self.title = title
#         self.question = []
#         self.user_score = 0
#
#     def load(self):
#         with open('score.json', 'r') as file:
#             db = json.load(file)
#             return db
#
#     def get_name(self):
#         first_name = input('Enter your first name: ')
#         last_name = input('enter your last name: ')
#         self.username = f'{first_name} {last_name}'
#         return self.username
#
#     def add_question(self, question):
#         self.question.append(question)
#
#     def start_exam(self):
#         for i, question in enumerate(self.question,1):
#             print(f'{i}:{question.question_text}')
#             for idx,option in enumerate(question.options,1):
#                 print(f'{idx}.{option}')
#
#             answer=int(input('Enter your answer: '))
#             if question.check_answer(answer):
#                 print('your answer is correct')
#                 self.user_score +=1
#             else:
#                 print('wrong answer')
#         print(f'your total score: {self.user_score}')
#         self.save_result()
#
#     def save_result(self):
#         db=self.load()
#
#         result = {
#             'Username' : self.username,
#             'exam_title': self.title,
#             'user_score': self.user_score
#         }
#         db.append(result)
#
#         with open('score.json', 'a') as file :
#             json.dump(result,file,indent=4)
#             print('saved')

# exam = Exam('test exam')
# question1 = Question(
#     'where is the capital of france?',
#     ['1)europe','2)italy','3)paris','4)none'],
#     3
# )
#
# question2 = Question(
#     'how many continent do we have ? ',
#     ['1)5','2)6','3)7','4)8'],
#     4
# )
#
# question3 = Question(
#     'what is the official language of iran?  ',
#     ['1)arabic','2)farsi','3)french','4)turkish'],
#     2
# )
#
# question4= Question(
#     'where is the capital of italy? ',
#     ['1)vanice','2)florance','3)milan','4)rome'],
#     4
# )
#
# question5= Question(
#     'how many fingers do we have ?',
#     ['1)5','2)3','3)8','4)4'],
#     1
# )

# exam.add_question(question1)
# exam.add_question(question2)
# exam.add_question(question3)
# exam.add_question(question4)
# exam.add_question(question5)
#
# exam.start_exam()

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

        #     else :
        #         print('main password is not correct ‼️')
        #         print('---' * 10)
        #         return
        # print('Username not founded ‼️')
        # print('---' * 10)

        # for i in db:
        #     username = input('Enter your username :')
        #     sq1 = input('Where were you born ? :')
        #     sq2 = input('What is 4*5 ? :')
        #     if i['Username '] == username and sq1 == 'iran' and sq2 == '20':
        #         new_password = input('Enter your new password :')
        #         with open('db.json', 'w') as file:
        #             json.dump(db, file, indent=4)
        #         print('Password Changed✅')
        #         print('---' * 10)
        #         return username, sq1, sq2, new_password
        #     else:
        #         print('main password is not correct‼️')
        #         print('---' * 10)
        #         return
        # print('Username not founded‼️')
        # print('---' * 10)

# class exam :
#     def __init__(self):
#         self.exam, self.test = self.final()
#
#     def final(self):
#

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

# signup = register()
# signup.write()

# login = Login()
# login.write()

main = main()
main.main()
# main.write()