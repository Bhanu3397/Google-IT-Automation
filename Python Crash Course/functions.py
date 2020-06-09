def greeting(name):
    #parameters/arguments are passed as string
    print("Hello "+ name)
greeting("Stranger") #here we are passing name as string

def greeting(name,age):
    print('Hello '+ name)
    print('So, you are '+age+ ' old haa!')
greeting("Stranger","27")

#returning values from a fuction so we can use it later

def area_triangle(base, height):
    return base*height/2
#here we are using retun keyword to return the values so we can use them.
# we are passing integers here as parameters    
area_a = area_triangle (5,4)
area_b = area_triangle(10,4)
total_area = area_a+area_b
#we are converting total_area to a string to avoid the sting and int Concatenation error
#because we can't Concatenation sting and int unless you change the type(data type) 
print("The sum of both areas is: "+ str(total_area))

#with return in function you can return more than one value.
def convert_sce(seconds):
    # // is floor division return the divided value 
    #example 60//10 returns 6 not the remeinder value
    hours = seconds // 3600
    minutes = (seconds - hours*3600)//60
    remaining_seconds = seconds - hours *3600 - minutes*60
    return hours,minutes,remaining_seconds
hours,minnutes,remaining_seconds = convert_sce(3500)
print(hours,minnutes,remaining_seconds)

#you can return nothing from functions these are called NONE type
def greeting(name):
    #parameters/arguments are passed as string
    print("Hello "+ name)
#insted of calling greeting() function, we can assign greeting function to a variable
result = greeting("Stranger")
#if you try to print result now, that will return None
#because we are not returning anything from the function.
print(result)


# Recursive function

def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n
    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
print(sum_positive_numbers(1)) # Should be 1
