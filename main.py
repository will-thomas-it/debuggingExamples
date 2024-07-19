# Debugging Odd Even
# Intial Code
number = int(input()) 
if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

# Error was in Line 4: missing a single '='.
# Single '=' is for assignment, double '=' is for checking quality.
# Debugged Code
number = int(input())
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
###############################################

# Debugging Leap Year
# Intial Code
year = input()
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

# Error was in Line 22: TypeError without int() conversion
# Debugged Code
year = int(input())
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
###############################################

# Debugging FizzBuzz
# Intial Code
target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])

# Error in Line 54: use 'and' (not 'or')
# Errors in Lines 56 & 58: use 'elif' (not 'if')
# Error in Line 61: remove square brackets from '([number])
# Debugged Code
target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
