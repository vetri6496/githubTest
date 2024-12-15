is_student = input("Are you a student (y/n): ")
is_pet = input("Do you have pets (y/n): ")
is_smoke = input("Do you smoke (y/n): ")

if is_student == 'y':
    student = True
else:
    student = False

if is_pet == 'y':
    pet = True
else:
    pet = False

if is_smoke == 'y':
    smoke = True
else:
    smoke = False



if student==True:
    if pet == False and smoke == False:
        print(f"You're a proper student and Property available")
    else:
        print("You're stduent but you smoke and have pet so not available")

elif student == False:
    if not smoke and not pet:
        print("You're not a student but you do both smoke and pet, so property Unavailable")
    else:
        print(f"You're not a student, Property Available")

