

with open ("list1.txt") as file:
    m = file.readline()

with open ("file2.txt") as file5:
    n = file5.readline()

List = [num for num in n if num in m]
print(m)
print(n)
print(List)