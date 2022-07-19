# Python program to count number of ways a given score could be reached 
# assuming the score is from a game where a move can earn 1, 5, or 10 points.
# Last Modified: 7/19/2022

print("This program will tell you the number of ways the score could have been reached.")
print ("Please enter a score. (whole numbers please)")

valid = True

#to ensure the number being input is a whole number
while valid:
  try:
    n = int(input("Score : "))
    
    valid = False
  except ValueError:
    print("That's not a whole number. Please input a whole number value for the score.")

def count(n): #number of ways to reach score n

  #table will store count of solutiions
  table = [0 for i in range(n+1)]

  table[0] = 1 #base case

  #consider each possible move one by one and update the table[] acordingly
  for i in range(1,n+1):
    table[i] += table[i-1]
  for i in range(5,n+1):
    table[i] += table[i-5]
  for i in range(10,n+1):
    table[i] += table[i-10]

  return table[n]

x = str(count(n))
num = str(n)
if count(n) == 1:
  print("The score is "+ num +" and can be reached " + x + " way.")
else:
  print("The score is "+ num +" and can be reached " + x + " ways.")

