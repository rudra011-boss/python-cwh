#ps3
#qn1
'''name = input("user_name :")
print(f"Good Afternoon {name}")'''
#qn2
"""name = input("NAME")
date = int (input("DATE"))
print (f''' Dear <|{name}|>
       You are selected!
       <|{date}>|''')""" #my way
"""(letter = '''Dear <|Name|>,
You are selected!
<|Date|> '''

print (letter.replace("<|Name|>","Harry").replace("<|Date|", "24 September 2050")) 
#we can make chains of .replace(" "," ")"""
#qn3
name = "my  name is raju paan walla"
print(name.find("  ")) #returns index of first occurance 
#in case no double space it returns -1,hence detected
#qn4
print(name.replace("  "," "))# Strings are immutable which means that you cannot change them by running functions on them
# qn5
letter = "Dear harry,\n\t this python course is nice.\n Thanks!"
print(letter)
# ps 4
# Qn 1
fruit = []
f1 = input("enter 1st fruit name :")
fruit.append(f1)
f2 = input("enter 2nd fruit name :")
fruit.append(f2)
f3 = input("enter 3rd fruit name :")
fruit.append(f3)
f4 = input("enter 4th fruit name :")
fruit.append(f4)
f5 = input("enter 5th fruit name :")
fruit.append(f5)
f6 = input("enter 6th fruit name :")
fruit.append(f6)
f7 = input("enter 7th fruit name :")
fruit.append(f7)
print(fruit)
