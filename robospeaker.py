import os

if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1 - Created by Bhavesh")
    os.system("say 'Welcome to Robospeaker 1.1, Created by Bhavesh'")
    while True:
        os.system("say 'Enter what you want me to pronounce'")
        x = input("Enter what you want me to pronounce: ")
        if x == "q":
            os.system("say 'bye bye friend'")
            break
        command = f"say {x}"
        os.system(command)
