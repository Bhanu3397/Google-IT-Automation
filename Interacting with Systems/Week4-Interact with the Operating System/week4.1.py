# This contains examples used in the course
def to_seconds(hours,mins,sec):
    return hours*3600+mins+sec 
print("welcome to this time converter")
cont = 'y'
while(cont.lower() == 'y'):
    hours = int(input('Enter no of hours: '))
    mins = int(input('Enter no of Mins: '))
    sec = int(input('Enter no of seconds: '))

    print('That is {} seconds'.format(to_seconds(hours,mins,sec)))
    print()
    cont = input("Do you want to do another conversion [enter y to continue]: ")

print("Good bye!")
