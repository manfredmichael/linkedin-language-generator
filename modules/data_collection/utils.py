import pickle, os
import getpass

AUTHENTICATION_PATH = '../../secrets/authentication'

class Authentication:
    def get_authentication(self):
        username, password = self.load_authentication()
        return username, password

    def load_authentication(self):
        if self.authentication_exist():
            with open(AUTHENTICATION_PATH, 'rb') as f:
                username, password = pickle.load(f)
        else:
            username, password = self.create_authentication()
        return username, password 

    def authentication_exist(self):
        return os.path.isfile(AUTHENTICATION_PATH)

    def create_authentication(self):
        print("Authentication doesn't exist. Please insert a new one..")
        username = getpass.getpass('username: ')
        password = getpass.getpass('password: ')
        with open(AUTHENTICATION_PATH, 'wb') as f:
            pickle.dump((username, password), f)
        return username, password


