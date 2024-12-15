def fruits():

    print("apple", "orange")
    print(1/0)


def main():
    try:
        fruits()
    except:
        print("Check for the error")
main()