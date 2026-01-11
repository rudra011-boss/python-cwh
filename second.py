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
