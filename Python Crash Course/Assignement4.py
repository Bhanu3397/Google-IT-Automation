host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys()) #prints keys "router""localhost""google"

#2
colors = ["red", "white", "blue"]
colors.insert(2, "yellow") #inserts yellow into 3rd index[2]=3. 
print(colors)

#The highlight_word function changes the given word in a sentence to its upper-case version. 
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". 
# Can you write this function in just one line?
def highlight_word(sentence, word):
	return(sentence.replace(word,word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

#Use a list comprehension to create a list of squared numbers (n*n). 
#The function receives the variables start and end, and returns a list of squares of consecutive numbers between start and end inclusively. 
#For example, squares(2, 3) should return [4, 9].
def squares(start, end):
	return [x**2 for x in range(start, end+1)]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. 
# Drew was the first one to note which students arrived, and then Jamie took over. 
# After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. 
# Jamie emailed a follow-up, saying that her list is in reverse order. Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.
def combine_lists(list1, list2):
  new_list=list2
  r=list(reversed(list1))
  new_list+=r
  return new_list
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

#solution 2 for upper problem
def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  new_list = list2
  for i in reversed(range(len(list1))):
    new_list.append(list1[i])
  return new_list

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
print(combine_lists(Jamies_list, Drews_list))

#The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". 
#The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". 
#Fill in the gaps to complete this function.
def format_address(address_string):
  # Declare variables
  house_number =''
  street_name =''
  # Separate the address string into parts
  spi = address_string.split()
  # Traverse through the address parts
  for ele in spi:
    # Determine if the address part is the
    # house number or part of the street name
    if ele.isdigit():
      house_number = ele
    else:
      street_name += ele
      street_name += ' '
  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

#Complete the code to iterate through the keys and values of the car_prices dictionary
#printing out some information about each one.
def car_listing(car_prices):
  result = ""
  for car,price in car_prices.items():
    result += "{} costs {} dollars".format(car,price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

#Updating or adding two dict together
def combine_guests(guests1, guests2):
   guests2.update(guests1)
   return guests2
  
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))