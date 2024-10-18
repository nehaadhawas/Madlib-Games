import random

def game():
  user = input("select one, 'r' for rock , 'p' for paper and 's' for sccissor:")
  computer = random.choice(['r','p','s'])
 
  
  if user == computer:
    return "It is a tie"
  
  if is_win(user,computer):
      return 'you win!'
    
  return "You lost!" 

def is_win(player, opponent):
  if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
    or (player == 'p' and opponent == 'r'):
    return True
  
  return False  

print(game())
