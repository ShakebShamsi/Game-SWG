# Sanke Water Gun Game or Rock Paper Scissor

import random
 
def game(comp, you):
    if comp == you:
        return None
    
    elif comp == "s":
        if you == "w":
           return False
        elif you == "g":
          return True  
      
    elif comp == "w":
        if you == "g":
           return False
        elif you == "s":
         return True    
    
    elif comp == "g":
        if you == "s":
           return False
        elif you == "w":
          return True    

print("Comp turn: Snake(s), Water(w), or Gun(g)?")
randomNo = random.randint(1,3)
if randomNo == 1:
   comp = "s"
elif randomNo == 2:
   comp = "w"   
elif randomNo == 3:
   comp ="g"   

you =input("Your turn: Snake(s), Water(w), or Gun(g)? \n")
a = game(comp, you)

print(f'Computer Chose: {comp}')
print(f'You Chose: {you}')

if a== None:
   print(f'The game is a tie')

elif a:
   print(f'You Win!')

else:
    print(f'You Lose!')
   
