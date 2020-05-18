# 1
number = 10
if number > 11: 
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)
#2
print((2**2) == 4)

#3
#If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, 
# can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = block_size // filesize
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = block_size % filesize
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * 2
    return block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192

#Complete the body of the format_name function. This function receives the first_name and last_name parameters and then returns a properly formatted string.
def format_name(first_name, last_name):

  if first_name != '' and last_name !='':

     return ("Name: " + first_name + ", " + last_name)

  elif first_name != ' ' or last_name !=' ':

     return ("Name: " + first_name + last_name)

  else:
     return ''

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string