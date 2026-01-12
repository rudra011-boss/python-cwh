#ps3
#qn1
'''name = int(input("user_name :"))
print(f"Good Afternoon {name}")'''
#qn2
"""name = int(input("NAME"))
date = int (int(input("DATE")))
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
'''( fruit = []
f1 = int(input("enter 1st fruit name :"))
fruit.append(f1)
f2 = int(input("enter 2nd fruit name :"))
fruit.append(f2)
f3 = int(input("enter 3rd fruit name :"))
fruit.append(f3)
f4 = int(input("enter 4th fruit name :"))
fruit.append(f4)
f5 = int(input("enter 5th fruit name :"))
fruit.append(f5)
f6 = int(input("enter 6th fruit name :"))
fruit.append(f6)
f7 = int(input("enter 7th fruit name :"))
fruit.append(f7)
print(fruit) )'''
#qn2
'''(marks = []
m1 = int(input("enter marks of 1st student:"))
marks.append(m1)
m2 = int(input("enter marks of 2nd student:"))
marks.append(m2)
m3 = int(input("enter marks of 3rd student:"))
marks.append(m3)
m4 = int(input("enter marks of 4th student:"))
marks.append(m4)
m5 = int(input("enter marks of 5th student:"))
marks.append(m5)
m6 = int(input("enter marks of 6th student:"))
marks.append(m6)
marks.sort()
print(marks))'''
#qn3
'''(T = (5,34,"om")
str(T[1])
print(type(T[1])))'''

#qn4
list = [5,6,4,2]
print(sum(list))

