#Fill in the blanks of this code to print out the numbers 1 through 7.
number = 1
while number < 7:
	print(number, end=" ")
	number +=1

#The show_letters function should print out each letter of a word on a separate line. 
# Fill in the blanks to make that happen.
def show_letters(word):
	for letter in word:
		print(letter)

show_letters("Hello")
# Should print one line per letter

#Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits.
# Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.
def digits(n):

    count = 0
    if n ==0:
        return 1
    while n != 0: 
        n //= 10
        count+= 1
    return count 
		
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

#This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column).
#  Fill in the blanks so that calling multiplication_table(1, 3) will print out:
#1 2 3
#2 4 6
#3 6 9
def multiplication_table(start, stop):
	for x in range(start,stop+1):
		for y in range(start,stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)


def first_and_last(message):
	if message == "":
		return True
	elif message[0] == message [-1]:
		return True
	else:
		return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

#Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case.
# For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

#Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam".
# For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".
def student_grade(name, grade):
	return ("{name} received {grade}% on the exam".format(name=name,grade=grade))

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

#Fill in the gaps in the nametag function so that it uses the format method to return first_name and the first initial of last_name followed by a period. 
# For example, nametag("Jane", "Smith") should return "Jane S."
def nametag(first_name, last_name):
	return("{} {}.".format(first_name,last_name[0].upper()))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 

#Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having only 1 decimal place. 
# For example, convert_distance(12) should return "12 miles equals 19.2 km".
def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km


def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for letter in input_string.strip():
        # Add any non-blank letters to the 
        # end of one string, and to the front
        # of the other string. 
        new_string = new_string+letter.replace(" ","")
        reverse_string = letter.replace(" ","")+reverse_string
    # Compare the strings
    if new_string.lower() == reverse_string.lower():
        return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

#unsolved 
def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the 
        # end with the new string
        i = len(old)
        new_sentence = sentence[:-i]+new
        return new_sentence
    # Return the original sentence if there is no match
    return sentence
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"

def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing

#The skip_elements function returns a list containing every other element from an input list, 
# starting with the first element. 
# Complete this function to do that, using the for loop to iterate through the input list.
def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0
	# Iterate through the list
	for element in elements: 
		# Does this element belong in the resulting list?
		if i%2 == 0:
			# Add this element to the resulting list
			new_list.append(element)
		# Increment i
		i += 1
	return new_list
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

#Let's use tuples to store information about a file: its name, its type and its size in bytes.
#Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.
def file_size(file_info):
	name, extension, size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

#Try out the enumerate function for yourself in this quick exercise. 
# Complete the skip_elements function to return every other element from the list, 
# this time using the enumerate function to check if an element is on an even position or an odd position.
def skip_elements(elements):
	# code goes here
	new_list = []
	index = 0
	for index,element in enumerate(elements):
	  if index%2 ==0:
	    new_list.append(element)
	    index +=1 
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']