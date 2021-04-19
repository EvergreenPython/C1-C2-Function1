# get Name function 
def getName(): 
	userName = input("Please tell me your name: ")
	# userName variable is specific to this function
	return userName 

def greetUser(name): # parameter variables are specific to the function 
	print("Hi " + name)
 
greetUser(getName())
greetUser(getName())
greetUser(getName())

# ask the user for two numbers 
#num1 = int(input("Please give me a number: "))
#num2 = int(input("Please give me a second number: "))

# write a function that takes num1 and num2 as parameters
# prints the sum 
def sum(numList): 
	total = 0 
	for index in numList: 
		total += index 
	print("The sum is " + str(total))

sum([1,2,3,4,5,6,7,8,9,10]) # 55

# function for product 
def product(numList): 
	total = 1 
	for index in numList: 
		total *= index 
	print("The product is " + str(total))

product([1,2,3,4,5,6,7,8,9,10])