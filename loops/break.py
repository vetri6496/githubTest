for i in range (10):

    print(f"The loop started ", i)
    flag = input("Do you want to continue the loop (y/n): ")
    if flag == 'n':
        break
    elif flag == 'y':
        print("y is prssed")
        continue
        # print(f"The loop ending is ", i)

print(f"Completed !")

