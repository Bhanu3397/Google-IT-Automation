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
#The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5. 
# An additional requirement is that the result is not to exceed 25, which is done with the break statement. 
# Fill in the blanks to complete the function to satisfy these conditions.
def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number*multiplier 
		# What is the additional condition to exit out of the loop?
		if result >25:
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier+= 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24


def sum_divisors(n): 
    sum = 0
    z = 1

    while n > z:
        if n % z == 0:
            sum = sum + z
            z = z + 1
        else:
            z = z + 1
    # Return the sum of all divisors of n, not including n
    return sum
print(sum_divisors(0)) 
print(sum_divisors(45))

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(1,x):
        print(square(n))
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285


def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = i*result
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

# Nested loops
teams = ['dragons','pandas','wolves','unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team+" VS "+away_team)

#ans for Q1:
def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = x*result
    return result
for n in range(0,10):
    print(n, factorial(n))

#ans for Q2:
def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)

#ans for Q3
for x in range(0,15):
  print(x*7)


#ans for Q4
def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)