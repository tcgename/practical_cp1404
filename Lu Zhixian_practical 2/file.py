#1.
in_file = open("name.txt","r")

#2.
in_file.read()
print("Your name is Stephen Strange")
in_file.close()

#3.
num_file = open("numbers.txt","r")
for i in [17,42,400]:
    print(i)
add = 17 + 42
print(add)
num_file.readline()
num_file.close()


