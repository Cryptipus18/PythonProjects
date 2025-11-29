import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')


#class
class Player:
    def __init__(self,hp,ep,name,num,move=None):
        self.name = name
        self.hp = hp
        self.ep = ep
        self.num = num
        self.move = move

#moves
costs = {"A": 6,
        "B": 25,
        "C": 10,
        "D": 13,
        "E": 0
}

dmg = {"A": 10,
       "B": 40,
       "C": 0,
       "D": 6,
       "E": 0
}



#matchups
p1_moves = {"A", "B", "C", "D", "E"}
p2_moves = {"A", "B", "C", "D", "E"}

#functions
def display(player1,player2,round):
    print(f"\n=== Night {round} ===")
    print("==========")
    print("Player Status")
    print("----------")
    print(f"Player 1 ({player1.name})")
    print(f"Health: {player1.hp}")
    print(f"Energy: {player1.ep}")
    print("----------")
    print(f"Player 2 ({player2.name})")
    print(f"Health: {player2.hp}")
    print(f"Energy: {player2.ep}")
    print("==========")
            
    print("\nAvailable Moves:"
          "\nA. Dagger Slash (10 damage; energy: 6)"
          "\nB. Vampiric Claws (40 damage; energy: 25)"
          "\nC. Dodge: Bat Form (nullifies incoming attack; energy: 10)"
          "\nD. Drain Life (deals 6 damage then heals self by 10; energy: 13)"
          "\nE. Do nothing (energy: 0)"      
                )
            
    print("\nPlayers, What are your moves?")
    print("Please enter A, B, C, D, or E only\n")

#matchups results
def check_p2dodges(player1,player2):
    player1.ep -= costs[player1.move]
    player2.ep -= costs[player2.move]
    print("\nMove Effects: ")
    print(f"Player 1 {player1.name} uses {costs[player1.move]} energy.")
    print(f"Player 2 {player2.name} received 0 damage.")
    print(f"Player 2 {player2.name} uses {costs[player2.move]} energy.")
    print(f"Player 1 {player1.name} received 0 damage.")

def check_p1dodges(player1,player2):
    player1.ep -= costs[player1.move]
    player2.ep -= costs[player2.move]
    print("\nMove Effects: ")
    print(f"Player 1 {player1.name} uses {costs[player1.move]} energy.")
    print(f"Player 2 {player2.name} received 0 damage.")
    print(f"Player 2 {player2.name} uses {costs[player2.move]} energy.")
    print(f"Player 1 {player1.name} received 0 damage.")

def both_dodges(player1,player2):
    player1.ep -= costs[player1.move]
    player2.ep -= costs[player2.move]
    print("\nMove Effects: ")
    print(f"Player 1 {player1.name} uses 10 energy.")
    print(f"Player 2 {player2.name} received 0 damage.")
    print(f"Player 2 {player2.name} uses 10 energy.")
    print(f"Player 1 {player1.name} received 0 damage.")

def atk_matchups(player1,player2):   
    player2.hp -= dmg[player1.move]
    player1.hp -= dmg[player2.move]
    player1.ep -= costs[player1.move]
    player2.ep -= costs[player2.move]
    if player1.move == 'D' and player2.move != 'D':
        player1.hp += 10
        print("\nMove Effects: ")
        print(f"Player 1 {player1.name} uses {costs[player1.move]} energy")
        print(f"Player 2 {player2.name} received {dmg[player1.move]} damage.")
        print(f"Player 2 {player2.name} uses {costs[player2.move]} energy.")
        print(f"Player 1 {player1.name} received {dmg[player2.move]}, and healed for 10 health points.")
    elif player2.move == 'D' and player1.move != 'D':
        player2.hp += 10
        print("\nMove Effects: ")
        print(f"Player 1 {player1.name} uses {costs[player1.move]} energy.")
        print(f"Player 2 {player2.name} received {dmg[player1.move]}, and healed for 10 health points.")
        print(f"Player 2 {player2.name} uses {costs[player2.move]} energy.")
        print(f"Player 1 {player1.name} received {dmg[player2.move]} damage.")  

    elif player1.move == 'D' and player2.move == 'D':
        player1.hp += 10
        player2.hp += 10

        print("\nMove Effects: ")
        print(f"Player 1 {player1.name} uses {costs[player1.move]} energy.")
        print(f"Player 2 {player2.name} received {dmg[player1.move]} damage, and healed for 10 health points.")
        print(f"Player 2 {player2.name} uses {costs[player2.move]} energy.")
        print(f"Player 1 {player1.name} received {dmg[player2.move]}, and healed for 10 health points.")
    else :    
        print("\nMove Effects: ")
        print(f"Player 1 {player1.name} uses {costs[player1.move]} energy.")
        print(f"Player 2 {player2.name} received {dmg[player1.move]} damage.")
        print(f"Player 2 {player2.name} uses {costs[player2.move]} energy.")
        print(f"Player 1 {player1.name} received {dmg[player2.move]} damage.")    

def idle_move(player1,player2):

    player2.hp -= dmg[player1.move]
    player1.ep -= costs[player1.move]
    if player1.move == 'D':
        player1.hp += 10
        print("\nMove Effects: ")
        print(f"Player 1 {player1.name} uses {costs[player1.move]} energy.")
        print(f"Player 2 {player2.name} received {dmg[player1.move]} damage.")
        print(f"Player 2 {player2.name} uses {costs[player2.move]} energy.")
        print(f"Player 1 {player1.name} received {dmg[player2.move]}, and healed for 10 health points.")
    else :    
        print("\nMove Effects: ")
        print(f"Player 1 {player1.name} uses {costs[player1.move]} energy.")
        print(f"Player 2 {player2.name} received {dmg[player1.move]} damage.")
        print(f"Player 2 {player2.name} uses {costs[player2.move]} energy.")
        print(f"Player 1 {player1.name} received {dmg[player2.move]} damage.")
    
    if player2.move in ["A", "B", "D"] and player1.move == "E":
        player1.hp -= dmg[player2.move]
        player2.ep -= costs[player2.move]
        if player2.move == 'D':
            player2.hp += 10
            print("\nMove Effects: ")
            print(f"Player 1 {player1.name} uses {costs[player1.move]} energy.")
            print(f"Player 2 {player2.name} received {dmg[player1.move]}, and healed for 10 health points.")
            print(f"Player 2 {player2.name} uses {costs[player2.move]} energy.")
            print(f"Player 1 {player1.name} received {dmg[player2.move]} damage.")
        else :    
            print("\nMove Effects: ")
            print(f"Player 1 {player1.name} uses {costs[player1.move]} energy.")
            print(f"Player 2 {player2.name} received {dmg[player1.move]} damage.")
            print(f"Player 2 {player2.name} uses {costs[player2.move]} energy.")
            print(f"Player 1 {player1.name} received {dmg[player2.move]} damage.")
    else : 
        print("\nMove Effects: ")
        print(f"Player 1 {player1.name} uses {costs[player1.move]} energy.")
        print(f"Player 2 {player2.name} received {dmg[player1.move]} damage.")
        print(f"Player 2 {player2.name} uses {costs[player2.move]} energy.")
        print(f"Player 1 {player1.name} received {dmg[player2.move]} damage.")


   

def turncal(player1,player2):
    if player1.move in {"A","B","D","E"} and player2.move == "C":
        check_p1dodges(player1,player2)
    elif player2.move in {"A","B","D","E"} and player1.move == "C": 
        check_p2dodges(player1,player2)
    elif player1.move == "C" and player2 == "C":  
        both_dodges(player1,player2)
    elif player1.move in {"A","B","D"} and player2.move in {"A","B","D"}:    
        atk_matchups(player1,player2)
    elif player1.move in ["A", "B", "D"] and player2.move == "E":
        idle_move(player1,player2) 
    if player1.ep < 0:
        player1.ep = 0
    if player2.ep < 0:
        player2.ep = 0


#battle sequence
def get_player_move(player):
    while True:
        player.move = input(f"Player {player.num} ({player.name}): ").upper().strip()
        if player.move in {"A", "B", "C", "D", "E"}:
            return player.move
        else:
            print("Invalid move. Please enter A, B, C, D, or E.")


def ep_to_cast(player1,player2):
    if player1.ep > 0 :
        get_player_move(player1)
    else :
        print(f"Player 1 {player1.name} has no more energy. Skipping this turn...")
        player1.move = None

    if player2.ep > 0 :
        get_player_move(player2)
    else : 
        print(f"Player 2 {player2.name} has no more energy. Skipping this turn...")
        player2.move = None


def check_rest(player):
    
    if player.ep > 0 :
            
        print(f"Player {player.num} {player.name} is able to have a complete rest.")
        print(f"Player {player.num} {player.name} heals for 25 and replenishes 20 energy.")  
        player.hp += 25
        player.ep += 20
        if player.ep > 50 :
            player.ep = 50
            
    else : 
            
        print(f"Player {player.num} {player.name} is too tired, and can only rest partially...")
        print(f"Player {player.num} {player.name} heals for 20 and replenishes 13 energy.")            
        player.hp += 20
        player.ep += 13
        if player.ep > 50 :
            player.ep = 50
            
            


def decide_winner(player1,player2):
    print("==========")
    if player1.hp <= 0 and player2.hp <= 0:
        print("Both players have been knocked out. It's a tie!")
    elif player1.hp <= 0:
        print(f"Player 2 {player2.name} wins! Player 2 ascends to a Vampire Lord...")
    else:
        print(f"Player 1 {player1.name} wins! Player 1 ascends to a Vampire Lord...")


def play_again(player1,player2):
    print("Would you like to play again?")
    print("Type Y to play again or N to exit.")
    while True:
        replay = input("Your choice: ").upper()
        if replay == "Y":
            clear_screen()
            player1.hp = 100
            player1.ep = 50
            player2.hp = 100
            player2.ep = 50
            start()
            break
        elif replay == "N":
            print("Thank you!")
            break
        else:
            print("Invalid input. Please type Y to play again or N to exit.")


def battlesequence(player1, player2):
    _round = 1
    while player1.hp > 0 and player2.hp > 0:
        display(player1,player2,_round)

        ep_to_cast(player1,player2)
        
        turncal(player1,player2)
        

        if _round % 3 == 0 and player1.hp > 0 and player2.hp > 0:
            print("\n3 nights have passed. Both vampire spawns shall rest...")  
            check_rest(player1)
            check_rest(player2)
        
        _round += 1
    decide_winner(player1,player2)
    play_again(player1,player2)


#variables
Player_1 = Player(100,50,None,1)
Player_2 = Player(100,50,None,2)


#start
def start():
    clear_screen()
    print("Welcome Vampire Spawn!")
    print("Fight for the right to ascend into a Vampire Lord")
    print("Attempt to knock your opponent.")
    print("Use your vampiric moves to outsmart your opponent.")

    print("\nPlayer, enter your names...")
    Player_1.name = input("Player 1: ")
    if Player_1.name == "" :
        Player_1.name = "player1"
    Player_2.name = input("Player 2: ")
    if Player_2.name == "" :
        Player_2.name = "player2"
    
    print("\nLet the duel between " + Player_1.name + " and "+ Player_2.name + " begin!" )
    clear_screen()
    battlesequence(Player_1,Player_2)


##########################3
start()