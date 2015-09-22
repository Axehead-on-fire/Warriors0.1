# --- Warriors 0.1 ---
# --- Non graphical Python Game Practice ---
# --- Python 3.2.5 ---
# --- John Hughes ---
# --- Started September 2015
# --- Last worked on 9/22/2015 ---


# --- SETUP ---

# Random is only module needed so far
import random

# Setup user profile
name = ""
while not name:
    name = input("What's your name? ")
print()

# Inventories
userInv = []
batInv = []

# Variables    name       hp     atk     inv
user =       [name,      10000, 1000, userInv]
bat =        ["Bat",      1000,  500,  batInv]
wolf =       ["Wolf",     1500, 1000, wolfInv] # Add random player picking






# --- MAIN LOOP ---

# Initialize sentry variable
game = True


while game == True:
    decision = input("(F)ight \n(I)nventory \n(P)rofile \n(Q)uit\n\n")
    f = "F"
    i = "I"
    p = "P"
    q = "Q"
    
    ### QUIT GAME ###
    if decision == q.lower():
        print ("Goodbye.")
        game = False
        
    ### PROFILE PAGE ###
    elif decision == p.lower():
        print ("\nName = " + name + \
               "\nHitpoints = " + str(user[1]) + \
               "\nAttack = " + str(user[2]) + \
               "\n\n")

    ### INVENTORY PAGE ###
    elif decision == i.lower():
        if userInv:
            print(str(userInv))
        else:
            print("You don't have any items yet.")
        
    ### FIGHT ###
    elif decision == f.lower():
        
        # atk function 
        def atk(atker, defender):
            """
            Subtracts the users atk from the enemy's hitpoints.
            Aka attacks the enemy.
            """
           
            atkerHits = random.randrange(atker[2])
            defender[1] -= atkerHits
            if defender[0] != name and defender[1] <= 0:
                print("You killed " + str(defender[0]) + " and win with " + \
                      str(atker[1]) + " hp left.")
                
            elif defender[0] == name and defender[1] <= 0:
                print ("You have died.")
                
            else:
                print (atker[0] + " hits " + str(defender[0]) + " " + \
                       str(atkerHits) + " hitpoints.")
                print (defender[0] + ": " + str(defender[1]) + " Hitpoints.\n")
            return defender[1]
        atk(user, bat)
        atk(bat, user)
