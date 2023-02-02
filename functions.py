import random

"""
Insert your function definitions in function definitions section
"""

# Number Functions

# Get an integer from the user
def getInt():
  while True:
    
    num = input("Please enter an integer\n")
    
    try:
      return int(num)
      break
    except: 
      print("This is not an integer\n")

# Get a decimal from the user
def getDecimal():
  while True:
    
    num = input("Please enter a decimal\n")
    
    try:
      float(num)
      try: 
        int(num)
        print("This is not a decimal\n")
      except: 
        return float(num)
        break
    except: 
      print("This is not a number\n")

# Get any number from the user
def getNumber():
  while True:
    
    num = input("Please enter a number\n")
    
    try:
      float(num)
      
      # If possible, return as an integer
      try: 
        return int(num)
      except:
        return float(num)
      break
      
    except: 
      print("This is not a number")
        



########## Function Definitions ##########

# 1. hello()
# Print out the words “Hello World!”

def hello():
  print("Hello World!")

# 2. helloPlus()
# Print out the word “Hello” followed by whatever additional text the user provides

def helloPlus():
  addWord = input('Enter any text you want\n')
  print("Hello " + addWord)
  
# 3. decSquare()
# Return the value of a decimal number, provided by the user, squared

def decSquare():
  print(getDecimal()**2)
  
# 4. intProd15()
# Return the product of an integer number provided by the user and 15

def intProd15():
  print(getInt() * 15)
  
  
# 5.decProd()
# Return the product of two decimal numbers provided by the user

def decProd():
  print("Decimal 1\n")
  num1 = getDecimal()
  
  print("Decimal 2\n")
  num2 = getDecimal()
  
  print(float(num1) * float(num2))

  
# 6. remainder()
# Return the remainder of an integer numerator and divisor provided by the user (remember the modulo operator)

def remainder():
  print("Integer 1\n")
  num1 = getInt()
  
  print("Integer 2\n")
  num2 = getInt()
  
  print(int(num1) % int(num2))
       
  
# 7. timesTable()
# Print the times table (from 0 to 10) of a number provided by the user

def timesTable():

  # Note: I have been instructed to just get an integer instead of a number
  num = getInt()

  i = 0
  listOfProducts = ""
  
  for x in range(i, 11):
    listOfProducts += str(num * int(x))
    if x < 10:
      listOfProducts += ", "
    i += 1
  print(listOfProducts)

# 8. randomNum()
# Print a random number

# Note from Alekz: In order to simplify this, I will make it a number between 1 and 10000

def randomNum():
  print(random.randint(1, 10000))

# 9. manyRandNum()
# Print as many random numbers as indicated by an integer provided by the user

def manyRandNum():
  num = getInt()

  listOfNumbers = ""
  for i in range(0, num):
    listOfNumbers += str(random.randint(1, 10000))
    if i < (num - 1):
      listOfNumbers += ", "
      
  print(listOfNumbers)

  # Note to self: Put the rest of the function AFTER the try except

  
# 10. randRange()
# Return a random integer from 0 to a number provided by the user

def randRange():
  print("This will generage a number from 0 to whatever you want")
  num = getNumber()

  # Uniform returns a random float between a range
  print(random.uniform(0, num))
  
  
# 11. randUserRange()
# Return a random integer between two numbers provided by the user

def randUserRange():
  print("This will generate an integer in the range you specify\n")

  print("First integer")
  num1 = getInt()

  print("Second integer")
  num2 = getInt()

  print(random.randint(num1, num2))

  
  
# 12. letsCount()
# Print the number 1, then ask if the user wants to print the next number. Repeat, adding 1 to the number each time, until the user inputs 'n'

def letsCount():

  
  i = 1
  # Initial counter
  print(i)
  
  while True:
    getInput = input("Would you like to increase the count? [Y/N]\n").upper()

    if getInput == "Y" or getInput == "N":
      if getInput == "Y":
        i += 1
        
      else:
        #Will only run if the input is "N"
        break
        
    else:
      print("That is not a valid input\n")
      #Loop
      continue

    # Will only print if the input is "Y". Loop ends if input is N and will restart if the input was not expected
    print(i)

  
# 13. sumThree()
# Return the sum of 3 numbers provided by the user

def sumThree():
  print("This will print out the sum of 3 numbers of your choice")
  
  print("First Number")
  num1 = getNumber()
  
  print("Second Number")
  num2 = getNumber()
  
  print("Third Number")
  num3 = getNumber()

# NOTE TO SELF: Attempted this, however an using int() will round a decimal DOWN by default. For future reference, check to see if the answer is not a decimal before attempting to print as an integer using try except
  
  valueAsInt = int(num1 + num2 + num3)
  valueAsDec = num1 + num2 + num3
  print(valueAsInt if (valueAsDec - valueAsInt) == 0 else valueAsDec)
  
  
# 14. sumMany()
# Return the sum of an arbitrary (unspecified) number of integers provided by the user. You will know the user has finished entering numbers when the user enters 0. 

def sumMany():
  print("This function will add every integer you input together until you have entered a 0\n")

  sum = 0

  while True:
    addAmount = getInt()
    if addAmount == 0:
      break
    else: 
      sum += addAmount

  print(sum)
  
# 15. minNums()
# Return the minimum of two numbers provided by the user

def minNums():
  print("Will return the lower of two numbers of your choice\n")

  num1 = getNumber()
  num2 = getNumber()

  if num1 < num2:
    print(num1)
  else:
    print(num2)
  
  
# 16. maxManyNums()
# Return the maximum number of an arbitrary set of integers input by the user. You will know the user is finished entering numbers when the user enters 0. 

def maxManyNums():
  print("Will take inputs until given a 0. Will then output the highest number out of those inputted\n")
  
  listOfNumbers = []

  while True: 
    num = getNumber()
    if num == 0:
      break
    else: 
      listOfNumbers.append(num)

  print(max(listOfNumbers))
    
  
  
  
# 17. powerOfTwo()
# Return the value of 2 raised to the power of an integer provided by the user (2*2*2...)

def powerOfTwo():
  print("Will print 2 to the power of an inputted integer\n")
  num = getInt()

  print(2**num)
  
# 18. powerOfWho()
# Return the value of an integer provided by the user raised to the power of an integer provided by the user (# * # * #...)

def powerOfWho():
  print("Will print an integer to the power of another integer")
  
  print("First Integer")
  num1 = getInt()

  print("Second Integer")
  num2 = getInt()

  print(num1**num2)
  
  
# 19. upperMe()
# Return the upper case value of a lower case character provided by the user (you'll need to do some research)

def upperMe():
  print("Will upper case any letter inputted\n")
  while True:
    letter = input("Please input a letter\n")

    if letter.isalpha():
      if len(letter) > 1:
        print("Please only input one letter\n")

      else: 
        print(letter.upper())        
        # A demonstration of bitwise operations to perform very fast toUpper
        # This is hard to read and should probably never be used unless you
        # know you need really, really tight optimization for run speed

        # print(chr(ord(list(letter)[0]) & ~(1<<5)))
        # a     0110 0001
        # A     0100 0001
        # 1     0000 0001
        # 1<<1  0000 0010
        # 1<<2  0000 0100
        # 1<<3  0000 1000
        # 1<<4  0001 0000
        # 1<<5  0010 0000
        break
        
    else:
      print("That is not a letter\n")