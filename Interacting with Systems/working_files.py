import os
import datetime
#os.remove("Interacting with Systems\os2.txt") # Removes file name called os2.txt
#os.rename("Interacting with Systems\operatingsystems1.txt","Interacting with Systems\os2.txt") #Renames file operating systems1 to os2 
#os.path.exists("Interacting with Systems\os2.txt") #checks if the os2 file exists or not
print(os.path.getsize("Interacting with Systems\os2.txt")) #File size in bytes 8bits = 1 byte
print(os.path.getmtime("Interacting with Systems\os2.txt")) # prints unix time stamp in seconds since (Jan 1st, 1970)
timestamp = os.path.getmtime("Interacting with Systems\os2.txt")
print(datetime.datetime.fromtimestamp(timestamp)) #formats the date and time to given format