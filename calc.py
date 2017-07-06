#functions
def add(x, y) :
  addition = float(x) + float(y)
  return addition
  
  
def mult (x, y) :
  return float(x) * float (y)
  
def div (x, y) :
  return float(x) / float(y)
  
def subs (x, y) :
  return float (x) - float(y)

#code for the calculator
q = 'y'

#while loop to keep going until the user wants to stop
while q == 'y' :

  print("enter 2 numbers to do math on!! ")
  
  a = input ('Enter the first number: ')
  b = input ('Enter the second number: ')

  words = { 'a' : float(a) + float(b), 'x' : float(a) * float (b), 'd' : float(a) / float (b), 's': float(a) - float (b)}
  
  func = input ('what function to run? ')
  print(func)
  print(words[func])
  
  #end of the while loop to make sure the user doesn't want to quit
  q = input ('Do you want to keep going? (y or n) ')
