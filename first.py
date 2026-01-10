print ("hello world")
a=2
b=3
c=a+b
print("C", c)
# practice set 1
# qn1
print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!
When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.
Twinkle, twinkle, little star,
How I wonder what you are!
Then the traveler in the dark
Thanks you for your tiny spark;
He could not see which way to go,
If you did not twinkle so.
Twinkle, twinkle, little star,
How I wonder what you are!
In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye
Till the sun is in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!
As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.
Twinkle, twinkle, little star,
How I wonder what you are! ''')
#qn4
import os

# Specify the directory path
path = "."

# List and print all contents of the directory
print("Contents of the directory:")
for item in os.listdir(path):
    print(item)
# ps2
# qn1
a = 1
b = 2
print (a + b)
# qn2
a=57
z = 7
print("the remainder we get on dividing a by z =", a%z)
# qn3
a = int(input("enter the value of a: "))
print (type(a))
#qn4
a = int(input("enter value of a : "))
b = int(input("enter value of b : "))
print("a is grater than b is ",a>b)
#qn5
a = float(input("enter value of a :"))
b = float(input("enter value of b :"))
print("the average of a and b is :",(a+b)/2)