PASSWORD = '1234'

def check_Password():

    for i in range (3):
        password = input("Enter the password: ")

        if password == PASSWORD:
            print("Access granted:")
            break
        else:
            print("Wrong password, Try again")

def welcome():
    print("Hello there !")


def main():
    welcome()
    check_Password()


main()
