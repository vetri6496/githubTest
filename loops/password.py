endlimit = 4

for i in range(1,endlimit):
    password = '12345'

    userPassword = input("Please Enter the password: ")

    if userPassword == password:
        print(f"Greetings user !")
        break
    else:
        print(f"Wrong password and you have ", (endlimit-1)-i , "attempt left")
        continue
