import os
import hashlib

def init():
    if not os.path.exists("./data/userdata"):
        os.makedirs("./data/userdata")
    if not os.path.isfile("./data/userdata/root"):
        os.remove("./data/userdata/*")
        f = open("./data/userdata/root", "w", encoding="utf-8")
        f.write("03f5bc7cd7a01de3a8d2f6462480b057")
        f.close()
        print("First time usage detected, please enter username and password to create a default user")
        username = input("Please enter username: ")
        passwd = input("Please enter password: ")
        md5 = hashlib.md5()
        md5.update(passwd.encode('utf-8'))
        password = md5.hexdigest()
        print("Successfully created default user: " + username)

    with open(f"./data/userdata/{username}", "w", encoding="utf-8") as f:
        f.write(password)