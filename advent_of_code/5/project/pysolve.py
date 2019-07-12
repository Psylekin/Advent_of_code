import string
import time
import smtplib, ssl

def connection_test():
    return 1

def react_polymer():
    for string in open ("advent_of_code/5/project/input.txt"):
        correctedString = correct_string(string)
        return (len(correctedString))

def correct_string(string):
    stringList = string_to_list(string)
    new_stringlist = edit_whole_stringList(stringList)
    correctString = list_to_string(new_stringlist)
    return correctString

def string_to_list(string):
    stringList = []
    for chars in string:
        stringList.append(chars)
    return stringList

def edit_whole_stringList(stringList):
    sameList = False
    while sameList == False:
        old_stringlist = stringList[:]
        new_stringlist = delete_double_entry(stringList)
        if len(old_stringlist) == len(new_stringlist):
            sameList = True
    return stringList

def delete_double_entry(stringList):
    for index in range(len(stringList) - 1):
        if must_destruct(stringList[index : index + 2]):
            del stringList[index : index + 2]
            break
    return stringList

def must_destruct(string):
    if string[0].capitalize() == string[1].capitalize():
        if string[0].isupper() and string[1].islower():
            return True
        elif string[0].islower() and string[1].isupper():
            return True
        else: 
            return False
    else:
        return False

def list_to_string(list):
    string = ''.join(list)
    return string


password = input("Type your password and press enter: ")
alphabet = list(string.ascii_lowercase)
highscore = ["",10774]

solutionstring = ""
for letter in alphabet:
    for string in open ("advent_of_code/5/project/input.txt"):
        shorter_string = string.replace(letter, "").replace(letter.swapcase(), "")
        solution = correct_string(shorter_string)
        if len(solution) < highscore[1]:
            highscore[0] = letter.upper()
            highscore[1] = len(solution)
        solutionstring += "Letter: {}    Length: {}\n".format(letter.upper(), len(solution))

print(solutionstring)
print(highscore)
# Sending Email because it takes so long.



def send_email(solutionstring, password):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "ben.lenkostendorf@gmail.com"  # Enter your address
    receiver_email = "bernardon@hotmail.de"  # Enter receiver address
    password = password
    message = """Subject: Deine Ergebnisse\n 

    {} \n
        
        
    LG Ben""".format(solutionstring)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
