TEXT = ("this is a collection of words of nice words this is a fun thing it is")
print(TEXT)

string = input("Enter what occurrences of the string you want: ")
while string != " ":
   if string in TEXT:
       word_to_count = {}
       for strings in string:
           if string in word_to_count:
               word_to_count[string] += 1
           else:
               word_to_count[string] = 1
           print("{}: {}".format(string, word_to_count))
   else:
       print("invalid string")
   string = input("Enter what occurrences of the string you want: ")

