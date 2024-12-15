def user_status():

    status = input("How are you doin: ")

    if status == 'Ok' or status == 'ok' or status == "OK":
        print("Good job !")
    else:
        print("You will be fine !")


user_status()