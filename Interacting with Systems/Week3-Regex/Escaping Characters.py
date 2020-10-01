import re
print(re.search(r"\.com","mydomain.com")) #\ uses for escape character.
print(re.search(r"\w*","This is an example")) # \w matches any alpha numeric characters including underscores
print(re.search(r"\w*","and_this_is_an_example"))

# \d matces digits, \b boundries, \s for matching whitespace characters
'''Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.'''
import re
def check_character_groups(text):
  result = re.search(r"\w*\d", text)
  return result != None
print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

print(re.search(r"A.*a","Argentina"))
print(re.search(r"A.*a$","Azerbaijan")) # None
print(re.search(r"A.*a$","Atlanta"))
pattern= (r"^[a-zA-Z_][a-zA-Z_]*$")
print(re.search(pattern,"_is_this_a_valid_variable_name"))
print(re.search(pattern,"is this a_valid_variable_name"))
print(re.search(pattern,"1_is_this_a_valid_variable_name"))

'''Fill in the code to check if the text passed looks like a standard sentence, 
meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point'''
import re
def check_sentence(text):
  result = re.search(r"^[A-Z ].*[.?!]", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

'''The check_web_address function checks if the text passed qualifies as a top-level web address,
meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), 
as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc.
Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.'''
import re
def check_web_address(text):
  pattern = r"\w\.com$|\.org|\.US"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

import re #Time format verification
def check_time(text):
  pattern = r'^[1-9][0-2]?:[0-5][0-9] ?[AM|PM|am|pm]'
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

import re #Zip code Verification
def check_zip_code (text):
  result = re.search(r"[^a-zA-Z][0-9]{5}|[0-9]{4}[-]", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False