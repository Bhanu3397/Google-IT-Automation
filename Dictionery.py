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

#Example 1 counting letters in repeted word #used for log analysis to check errors
def count_leters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter]+=1
    return result
a= count_leters("banana")
print(a)

#In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a list containing multiple values.
#Here we have a dictionary called "wardrobe" with items of clothing and their colors. 
#Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for cloth,colors in wardrobe.items():
	for color in colors:
		print("{} {}".format(color,cloth))

#The groups_per_user function receives a dictionary, which contains group names with the list of users. 
# Users can belong to multiple groups. 
# Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.
def groups_per_user(group_dictionary):
    user_groups = {}
    for group, users in group_dictionary.items():
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return user_groups

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

#The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. 
# Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).
def email_list(domains):
	emails = []
	for domain_name,users in domains.items():
	  for user in users:
	    emails.append("{}@{}".format(user,domain_name))
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

#The add_prices function returns the total price of all of the groceries in the dictionary. Fill in the blanks to complete this function.
def add_prices(groceries):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for price in groceries.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += price
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44