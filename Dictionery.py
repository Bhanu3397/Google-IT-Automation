toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"]=39 # Epilogue starts on page 39
toc["Chapter 3"]=24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc)# Is there a Chapter 5?
del toc["Chapter 3"] # Delete Chapter 3?
toc["Epilogue"] = 38 #Update a dictionary?
print(toc)

#Iteration over lists
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for name,orgon in cool_beasts.items():
    print("{} have {}".format(name,orgon))

#Example 1 counting letters in repeted word
def count_leters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter]+=1
    return result
a= count_leters("banana")
print(a)