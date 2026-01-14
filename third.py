#ps 5
#qn 1
'''(hindi_dict= {"नमस्ते": "Hello",
    "पानी": "Water",
    "किताब": "Book",
    "घर": "House",
    "स्कूल": "School",
    "दोस्त": "Friend"
}
word = int(input("int(input hindi words to see their english translation: "))
print("meaning =",hindi_dict.get(word)))'''
#qn2
'''(s = set()
n = int(input("enter number 1: "))
s.add(n)
n = int(input("enter number2: "))
s.add(n)
n = int(input("enter number 3: "))
s.add(n)
n = int(input("enter number 4: "))
s.add(n)
n = int(input("enter number 5: "))
s.add(n)
n = int(input("enter number 6: "))
s.add(n)
n = int(input("enter number 7: "))
s.add(n)
print(s))'''
#qn3
'''(s = set()
s.add(18)
s.add("18")
print(s) )'''
#qn4
'''(s = set ()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s)))'''
#qn5
'''(s = {}
print(type(s))'''
#qn6

'''(d = {}
name = input("enter friend name:")
lang = input("enter fav language :" )
d.update({name:lang})



name = input("enter friend name:")
lang = input("enter fav language :" )
d.update({name:lang})


name = input("enter friend name:")
lang = input("enter fav language :" )
d.update({name:lang})


name = input("enter friend name:")
lang = input("enter fav language :" )

d.update({name:lang})


print(d))'''
#qn9
# s = {8,7,12,"Harry",[1,2]}
#no we cant change the value of list inside a set.even we can't keep list as an element off set.
#elements in set shoud be imutable and hashable

# Quiz queation
a=int(input("enter yout age:"))
if(a>=18):
    print("you are above the age  of concent")
elif(a==0):
    print("zero can't be the age,please enter the valid age")

elif(a<0):
    print("please enter the valid age")
else:
    print("you are below the age of concent")

print("end of program")
