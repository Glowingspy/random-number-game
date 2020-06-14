#importing the module random
import random
import time
#giving value to the random 

#asking the user to guess the data



#if the value of y is greater than the random value then tell the user to think lower.
# if the value of y is lower than the random number then tell the user to think higher.
# define robi it is used to make another input




print('This is a GAME where you choose RANDOM numbers to START and END from, and then GUESS the one RANDOM NUMBER!!!!!!!')

def main_code():
    time.sleep(3)
    print('From what integer do you want to start from ?')
    time.sleep(1)
    print('Type your first integer where you want to start from')
    
    a = float(input())
    if a != int(a):
        print('Invalid.You typed something other than an integer. The program will restart in 3 seconds ')
        time.sleep(3)
        main_code()
    elif a == str(a):
        print('Invalid.You typed something other than an integer. The program will restart in 3 seconds ')
        time.sleep(3)
        main_code()    
    
    
    print('TYPE your second intger where you want the set of numbers to end')
    b = float(input())
    if b != int(b):
        print('Invalid.You typed something other than an integer. The program will restart in 3 seconds')
        time.sleep(3)
        main_code()
    
    
    
    
    x = random.randint(int(a), int(b))
    print('Guess an integer between ' + (str(a)) + ' and ' + (str(b)))
    y = int(input())
    if y == int(x) :
        print('You got the number. Do you want to play again')
        
   
    while y != x:
        if y > x:
            print('Think lower')
            y = int(input())
        elif y < x:
            print('Think higher')
            y = int(input())
            
    if y == x :
        print('You got the number. Do you want to play again') 
        time.sleep(1)
        print('Type "yes" or "no" ')
        z = input()
        if z == 'no':
            print('Get out of here!!!')
        elif z == 'yes':
            print('Ok')
            time.sleep(0.5)
            main_code()
        else:
            print('That is an invalid statment. Rerun the program if you wanted to start or exit if you said no.')
        
        # put a return function here







main_code()
























#x = 0 
#x += 1

#while True:
 #  print(x)
  # if x == 5:
   #   break






















#nums = [1,2,3,4,5]
#for num in nums:
 #   for letter in 'abc':
  #      print(num, letter)
        
    
    
    
    
    
    #if num == 3.00 :
     #   print('Found!')
      #  continue
    #print(num)