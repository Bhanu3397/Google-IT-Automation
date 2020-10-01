#Now we're going check out how to match these characters several times.
#So we wanted to find the longest word in the string, or we wanted to find the host names in a log file by checking for a bunch of alphanumeric characters between brackets. 
#We can do this using another interesting RegEx concept, repeated matches.
import re
print(re.search(r"py.*n","python")) # python
print(re.search(r"py.*n","python Programming")) #python Programmin because .* takes the whole string to the end.
#this is called grredy in python
print(re.search(r"py[a-z]*n","python")) #python
print(re.search(r"[a-z].*n","python")) #python #greedy
print(re.search(r"py[a-z]*n","Python Programming")) #none
print(re.search(r"py[a-z]*n","python Programming")) #python

#egrep +?
print(re.search(r"o+l+","goldfish")) #ol, one occurance each
print(re.search(r"o+l+","hollywood")) #oll
print(re.search(r"o+l+","woolly")) #ooll
print(re.search(r"o+l+","boil")) #None, there is a character between the o and l
print(re.search(r"p?each","They like each other")) #each, Here ? escapes or ignores 0 or 1 character before ?
print(re.search(r"p?each","They like peaches")) #peach

import re
def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None
print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True
