def student(id=100, name="MarkBoucher", mark=10.34):
    print(id, name, mark)
    print(type(id), type(name), type(mark))
def main():

    student(1, "name", 300.1)
    student(2, "John", 100.3)
    student(3, "Abhra", 50.5)
    student(4,"Cena")
    student("Amigty", 20)
    student()

main()