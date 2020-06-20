# linux command "grep" is based on regular expressions.
#circumflex -- "^" If you want to find a string that starts with we use "^" in fornt of the string.

#simple matching in python
#always use Rawstring in regex in python
import re
result=re.search(r"aza","plaza") #r represents Rawstring.
print(result)
result=re.search("aza","bazar")
print(result) 
print(re.search(r"^x","xenon"))
print(re.search(r"p.ng","penguin"))
print(re.search(r"p.ng","pong"))
print(re.search(r"p.ng","Pangaea",re.IGNORECASE)) #ignores case sensitive

#Fill in the code to check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between
def check_aei (text):
  #result = re.search(r"---", text)
  result = re.search(r"a.e.i", text)
  return result != None
print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

#Wildcards and Character Classes
#Character class is defined in []
print(re.search(r"[Pp]ython","Python"))
print(re.search(r"[a-z]way","This is the highway")) # hway
print(re.search(r"[a-z]way","This is a way")) #None because there is space between a and way
print(re.search(r"[a-zA-Z0-9]loud","Cloud")) #matches first character to a-z or A-Z or 0-9
print(re.search(r"cloud[a-zA-Z0-9]","cloud9")) #Matches last character to a-z or A-Z or 0-9

#Fill in the code to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.
import re
def check_punctuation (text):
  #result = re.search(r"___", text)
  result = re.search(r"[,.;:!?]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

#Match any characters that are not in group. To do that we use "^"
#Search any character that is not a letter
print(re.search(r"[^a-zA-Z]","There is a space between the line")) # prints first space in the line
print(re.search(r"[^a-zA-Z ]","There is a space between the line")) # None, because we excluded a-z and A-Z and spaces.
print(re.search(r"[^a-zA-Z ]","There is a space between the line.")) #prints "." because we did not excluded "." in the regex pattern.

# We can use "|" to match either or in the expression
print(re.search(r"cat|dog","I hate dogs")) #prints dog, because it search matches dog in the sentence
print(re.search(r"cat|dog","I hate cats")) # prints cat
print(re.search(r"cat|dog","I hate both cats and dogs")) # prints cat, because it search matches first word in the sentecnce 
print(re.search(r"cat|dog","I hate both dogs and cats")) # prints dog

# findall matches all posibilities in the sentence
print(re.findall(r"cat|dog","I hate both dogs and cats")) # prints a list ["dog","cat"]