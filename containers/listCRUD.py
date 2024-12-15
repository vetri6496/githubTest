menu = ["Display Database", "Add an item", "Delete and item", "Change an Item", "Quit"]

fruits = ["Apple", "Banana", "Orange"]

# TO DISPLAY THE ITEM
def menuitem():
    print("============================================")
    j=0
    for i in menu:
        j+=1
        print(j, ". ", i)


def display():
    print("-------------------------------------------")
    print("Here's the list of item in the list")
    for i in range (len(fruits)):
       print(i, ": ", fruits[i])

def additem():        
    item = input("Please enter the item to add: ")
    fruits.append(item)
    print("After adding" )
    display()
    

def deleteitem():
    display()
    number = int(input("Please Enter the item index to delete: "))

    if number > len(fruits):
        print("Invlaid index please enter the index")
    else:
        fruits.pop(number)
        print("After Deleting")
        display()

def updateitem():
    display()
    Itemtoupdate = input("Please enter the item to change: ")

    for i in range (len(fruits)):
        if Itemtoupdate == fruits[i]:
            updateItem = input("Enter new item name to replace: ")
            fruits[i]=updateItem

    print("After update")
    display()






def main():

    flag = True
    
    while flag == True:
        
        menuitem()
        selection = int(input("Please Enter the option: "))

        if selection == 1:
            display()
        elif selection == 2:
            display()
            additem()
        elif selection == 3:
            deleteitem()
        elif selection == 4:
            updateitem()    
        elif selection == 5:
            print("Quiting the program")  
            break  
        else:
            print("Enter the valid number")

main()