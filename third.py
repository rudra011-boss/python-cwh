#ps 5
#qn 1
hindi_dict= {"नमस्ते": "Hello",
    "पानी": "Water",
    "किताब": "Book",
    "घर": "House",
    "स्कूल": "School",
    "दोस्त": "Friend"
}
word = input("input hindi words to see their english translation: ")
print("meaning =",hindi_dict.get(word))
