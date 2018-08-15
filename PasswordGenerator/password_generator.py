import string as sg
import random
import json


class PassGenerator():
    file_name = None
    mypasslist = []

    def __init__(self, file_name):
        self.file_name = file_name
        while True:
            menu = self.input_control_error("""
            Please select an action:
            1 - Create new password
            2 - List passwords
            3 - Search password
            4 - Log Out
            """, is_numeric=True)
            if menu == 4:
	            exit()
            if menu == 1:
                self.register_new_pass()
            elif menu == 2:
                self.list()
            elif menu == 3:
                key = self.input_control_error("Search criteria :")
                self.search(key)
            else:
                print('Incorrect entry')

    def input_control_error(self, text, is_numeric=False):
        while True:
            input_data = input(text)
            if input_data.strip() != "":
                if is_numeric:
                    if input_data.isnumeric():
                        return int(input_data)
                    else:
                        print('Invalid entry')
                else:
                    return input_data
            else:
                print('Invalid entry')

    def register_new_pass(self):
        
        username = self.input_control_error("Please enter username :")
        password = input("Please enter passwords")
        if password.strip() == "":
            password_length = self.input_control_error('Please enter the password length', is_numeric=True)
            password = self.generate_pass(password_length)
        explanation = self.input_control_error("Enter a description :")

        self.mypasslist.append({"username": username, "password": password, "description": explanation})
        self.save()

    def edit(self,text,is_numeric=False):
       
        print('edit called')



    def load(self):
        
        with open(self.file_name) as file:
            print(file.read())
            file_data = file.read().strip().split("\n")
            for data in file_data:
                data_stack = data.split("@brackets@")
                self.mypasslist.append(
                    {"username": data_stack[0],
                     "password": data_stack[1],
                     "description": data_stack[2]})
        
    def list(self):
        
        for passlist in self.mypasslist:
            print(list(passlist.values()))

    def search(self, keyw):
        
        for passlist in self.mypasslist:
            if keyw in list(passlist.values()):
                print(list(passlist.values()))

    def save(self):
       
        with open(self.file_name, "w") as file:
            json.dump(self.mypasslist, file)

    def generate_pass(self, length):
        string_data = sg.printable
        return ''.join([string_data[random.randint(0, len(string_data) - 1)] for i in range(0, length)])


kep = PassGenerator("passfile.txt")
print(kep.generate_pass(10))
print(kep.load())