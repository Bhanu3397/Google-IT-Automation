#here we can see how we can write a function for this code to reduce to single line
#Functions help reduce the amount of code we write
name = "string"
number = len(name)*9
print("Hello "+name +" your lucky number is "+str(number))

name = "Avon Barksdale"
number = len(name)*9
print("Hello "+name +" your lucky number is "+str(number))

#function for the above code looks like this.
#And we can use this for any name.

def lucky_number(name):
    number = len(name)*9
    print("Hello "+name+" your lucky number is "+str(number))
lucky_number("String")
lucky_number("Avon Barksdale")

# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")

def month_days(month, days):
    print(month +" has "+ str(days)+ " days.")
#here we are passing month as string and days as integers and then converting days to string to concat
month_days("June",30)
month_days("July",31)
    