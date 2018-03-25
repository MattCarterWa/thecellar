import json
import os

user_email_to_id = "user_files_cellar/user_email_to_id.json"
user_folder = "user_files_cellar"

db = {
    "email": "id",
}

def get_new_user_id():
    new_user_id = "new_user_id.txt"
    #opens a file containing the newest available user number.
    #gives the requester that number.

    #Does not save the latest number until the user is saved.
    if not os.path.exists(os.path.join(user_folder, new_user_id)):
        print("Didn't find latest user id number")
        with open(os.path.join(user_folder, new_user_id), "w") as f:
            f.write("0")

    with open(os.path.join(user_folder, new_user_id), "r") as f:
        new_user_id = f.read()
        print("Getting latest user ID of ", new_user_id)

    return new_user_id

def user_finder_by_email(email):
    if not os._exists(user_email_to_id):
        with open(user_email_to_id, "w") as f:
            pass

    with open(user_email_to_id, "r") as f:
        email_list = json.loads(f)

        if email in email_list:
            user_path = os.path.join(user_folder, email_list[email]) + ".json"
            with open(user_path) as f:
                json_container = json.loads(f)
            return User(json_container)
        else:
            return None

class User:
    container = {
        "User ID": "",
        "Name": "",
        "Email": "",
        "Division": "",
        "Store": "",
        "Access Count": "",
        "Features Accessed": {}
    }

    def __init__(self, json_container):
        self.container = json_container

    @property
    def user_id(self):
        return self.container["User ID"]

    @property
    def name(self):
        return self.container["Name"]

    @property
    def email(self):
        return self.container["Email"]

    @property
    def division(self):
        return self.container["Division"]

    @property
    def store(self):
        return self.container["Store"]

    @property
    def access_count(self):
        return self.container["Access Count"]

    @property
    def features_accessed(self):
        return self.container["Features Accessed"]

    @name.setter
    def name(self, value):
        self.container["Name"] = value

    @email.setter
    def email(self, value):
        self.container["Email"] = value

    @division.setter
    def division(self, value):
        self.container["Division"] = value

    @store.setter
    def store(self, value):
        self.container["Store"] = value

    @access_count.setter
    def access_count(self, value):
        self.container["Access Count"] = value

    @features_accessed.setter
    def features_accessed(self, value):
        self.container["Features Accessed"] = value

    def set_new_user_ID(self):
        print("setting up new user")
        self.container["User ID"] = get_new_user_id()

    




def create_up_new_user(name, email, division, store):
    user = User(User.container)
    user.name = name
    user.email = email
    user.division = division
    user.store = store
    user.set_new_user_ID()

    return user


if __name__ == "__main__":
    user = create_up_new_user("Matt", "Blank@gmail.com", "701", "00688")
    print(user)







