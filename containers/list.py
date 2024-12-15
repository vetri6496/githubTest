fruits = ["apple", "orange", "mango"]
print(fruits)

fruits.append("banana")
print(fruits)

fruits.append("lime")
print(fruits)

fruits3 = fruits.copy()

# fruits[3]="strawberyy"
# print(fruits)


# fruits[:8] = ["kiwi"]
# print(fruits)


# fruits.insert(0,"gooseberry")
# print(fruits)

# fruits2=["new apple", "new mango"]

# fruits.extend(fruits2)
# print(fruits)

# fruits.remove("kiwi")
# print(fruits)

# fruits.pop(1)
# print(fruits)

# del fruits[1]
# print(fruits)

# fruits.clear()
# print(fruits)

# print(fruits3)

fruits4 = [i for i in fruits3]
print(fruits4)

fruits5 = [i+" " for i in fruits3]
print(fruits5)


fruits6 = [i for i in fruits3 if len(i) >5]
print(fruits6)