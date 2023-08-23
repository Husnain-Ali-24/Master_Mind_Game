import random
print("Now Player 1 setting a number and player 2 guess the number")
computer_guess=random.randint(1,10000)
digits=len(str(computer_guess))
Input1=int(input(f'Guess the {digits} number: '))
counter=0
condition=True
while condition==True:
 if Input1==computer_guess:
  print("Great! You guessed the number in just 1 try! You're a Mastermind!")
  condition=False
 elif Input1 != computer_guess:
  counter+=1
  count=0
  numbers=''
  for i in range(len(str(computer_guess))):
     if str(Input1)[i] == str(computer_guess)[i]:
       numbers+=str(Input1)[i]+" "
       count+=1
     else:
       numbers+="X"+" "
  print(f"Not quite the number. But you did get {count} digit(s) correct! Also these numbers in your input were correct.\n{numbers}")
  Input1=int(input("Enter Your Next Choice of Numbers: "))
  if Input1==computer_guess:
   print(f"Great! You guessed the number in {counter} try! You're a Mastermind!")
   condition=False
  elif Input1 != computer_guess:
   condition=True
print("Now Player 2 setting a number and player 1 guess the number")
computer_guess_1=random.randint(1,10000)
digits_1=len(str(computer_guess))
Input1_1=int(input(f'Guess the {digits_1} number: '))
counter_1=0
condition_1=True
while condition_1==True:
 if Input1_1==computer_guess_1:
  print("Great! You guessed the number in just 1 try! You're a Mastermind!")
  condition_1=False
 elif Input1_1 != computer_guess_1:
  counter_1+=1
  count_1=0
  numbers_1=''
  for i in range(len(str(computer_guess_1))):
     if str(Input1_1)[i] == str(computer_guess_1)[i]:
       numbers_1+=str(Input1_1)[i]+" "
       count_1+=1
     else:
       numbers_1+="X"+" "
  print(f"Not quite the number. But you did get {count_1} digit(s) correct! Also these numbers in your input were correct.\n{numbers_1}")
  Input1_1=int(input("Enter Your Next Choice of Numbers: "))
  if Input1_1==computer_guess_1:
   print(f"Great! You guessed the number in {counter_1} try! You're a Mastermind!")
   condition_1=False
  elif Input1_1 != computer_guess_1:
   condition_1=True
if counter>counter_1:
 print("Player 1 Win!")
elif counter<counter_1:
 print("Player 2 Win!")