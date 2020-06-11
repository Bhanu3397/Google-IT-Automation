#If you open a file for writing and the file already exists, the old contents will be deleted as soon as the file is opened.
with open("Interacting with Systems\write.txt","w") as file:
    file.write("hello love, It's nice meeting you again") # Write function overwrite whatever in the existing file

guests = open("Interacting with Systems\guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()

with open("Interacting with Systems\guests.txt") as guests:
    for line in guests:
        print(line)

new_guests = ["Sam", "Danielle", "Jacob"]

with open("Interacting with Systems\guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

with open("Interacting with Systems\guests.txt") as guests:
    for line in guests:
        print(line)

checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("Interacting with Systems\guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("Interacting with Systems\guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")
with open("Interacting with Systems\guests.txt") as guests:
    for line in guests:
        print(line)

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("Interacting with Systems\guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))