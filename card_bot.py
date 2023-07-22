
print("""===================================================================================
WELCOME TO THE CARD GAME :)
 - This is a card game developed by Sanat Tudu, Indrajit Kuli and Satish Kumar Oroan
===================================================================================\n""")

#===================================================== Modules ======================================================================================================================================

import random as r  # importing random module for the random selection of cards 
import collections  # importing collections module to use rotate function

prior = ["C","D","H","S"]                                           # priority order for the four different types of cards
prior2 = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]     # priority order for the each types of cards 
potw = ["J","Q","K","A"]                                            # The card required for determination of potential win

#==================================================== Functions =============================================================================================================================================================================

def read_sort():        # read the input file containing cards
    op = open("data.txt")
    data = op.readline()
    data = data.replace("\n","")
    data = data.split(",")
    lst = data.copy()
    data2 = []
    for x in range(len(lst)):
        data2.append(mini(data))
        data.remove(data2[x])
    return data2
    

def card_dis(total):    # this functions is to shuffle the deck of 52 cards then distribute serial wise properly to each players and returns 4 different list having 13 different cards in each list 
    r.shuffle(total)
    player1 = []        # creating list for 
    player2 = []        # to hold 13 cards 
    player3 = []        # for each players
    player4 = []
    count = 0
    for x in total:
        if count==0:
            player1.append(x)
            count = count+1
        elif count==1:
            player2.append(x)
            count = count+1
        elif count==2:
            player3.append(x)
            count = count+1
        elif count==3:
            player4.append(x)
            count = 0
        else:
            continue
    player1.sort() # just sorting the cards 
    player2.sort() # in numerical and alphabatic 
    player3.sort() # order ,note : the ordering is not   
    player4.sort() # in the actual priority sequencing of card  
    return player1,player2,player3,player4 

def illegal(inp,l,suit): # to check whether the user had enter the correct suit card or not
    if inp == "" :
        return True
    if check(suit,l):
        if inp[0].upper() == suit:
            return False
        else:
            return True
    else:
        return False


def valid(inp,l): # to check whether the element exist or not
    if inp in l:
        return False
    else:
        return True


def check(value,lst): # to check whether that given type of card is present or not and return Ture or False
    value2 = False
    for y in lst:
        if value in y:
            value2 = True
            break
    return value2

    
def display(lst,by): # to display the elemets of a given list in a defined manner 
    for x in lst:
        if lst.index(x) == len(lst)-1:
            print(x)
        else:
            print(x, end = by)

    
def maxi(l): # to find the highest valued card within the player
    count = 0
    m = -1
    maximum = ""
    val = ""
    if check("S",l):
        val = "S"
    elif check("H",l):
        val = "H"
    elif check("D",l):
        val = "D"
    elif check("C",l):
        val = "C"
    else:
        pass
    
    for x in l:
        if val in x :
            if prior2.index(x[1:])>m:
                maximum = x
                m = prior2.index(x[1:])
                
            else:
                continue
    return maximum

def maxi2(l,suit): # to find the highest card of same suit
    count = 0
    m = -1
    maximum = ""
    val = ""
    if check(suit,l):
        val = suit
    else:
        return mini(l)
    
    for x in l:
        if val in x :
            if prior2.index(x[1:]) > m:
                maximum = x
                m = prior2.index(x[1:])
                
            else:
                continue
    return maximum


def mini(l): # to find the lowest valued card within the player
    count = 0
    n = 13
    mnimum = ""
    val = ""
    if check("C",l):
        val = "C"
    elif check("D",l):
        val = "D"
    elif check("H",l):
        val = "H"
    elif check("S",l):
        val = "S"
    else:
        pass
    
    for x in l:
        if val in x :
            if prior2.index(x[1:])<n:
                minimum = x
                n = prior2.index(x[1:])
                
            else:
                continue
    return minimum    

def mini2(l,suit): # to find the lowest card of same suit
    count = 0
    n = 13
    mnimum = ""
    val = ""
    if check(suit,l):
        val = suit
    else:
        return mini(l)
    
    for x in l:
        if val in x :
            
            if prior2.index(x[1:])<n:
                minimum = x
                n = prior2.index(x[1:])
                
            else:
                continue
    return minimum    

def pot_win(l): # to find number of potential win for a player
    count = 0
    for x in l:
        if x[1] in potw:
            count = count + 1
    return count


def run(order,order2): # it is the main run function which collect card from each player, then determine which player has won and return the position of the winner
    lc = [" "," "," "," "]
    count = 0
    exiting = False
    
    while count < 4:
        if count == 0:
            if "bot" in order[count]:
                lc[0] = maxi(order2[order[0]])
                order2[order[0]].remove(lc[0])
            else:
                print("Your remaining cards are :",end = " ")
                display(order2[order[count]]," ")
                inp_card = input("Select your card : ")

                if quit(inp_card):
                    exiting = True
                    print("Play your last turn")
                    
                while valid(inp_card,order2[order[count]]) :
                    print("Illegal try !! \n")
                    inp_card = input("Select your card again : ")
                    
                lc[0] = inp_card
                
                order2[order[0]].remove(lc[0])
            suit = lc[0][0]
                
        else:
            if "bot" in order[count]:
                
                maxi_bot = maxi2(order2[order[count]],suit)

                if seq.index(max(lc)) < seq.index(maxi_bot):
                    lc[count] = maxi_bot
                    order2[order[count]].remove(lc[count])
                else:
                    mini_bot = mini2(order2[order[count]],suit)
                    lc[count] = mini_bot
                    order2[order[count]].remove(lc[count])
            else:
                print("Your remaining cards are :",end =" ")
                display(order2[order[count]]," ")
                inp_card = input("Select your card : ")

                if quit(inp_card):
                    exiting = True
                    print("Play your last turn")
                    
                while (illegal(inp_card,order2[order[count]],suit)) or valid(inp_card,order2[order[count]]):
                    
                    print("Illegal try !! \n")
                    inp_card = input("Select your card again : ")
                   
                lc[count] = inp_card
                order2[order[count]].remove(lc[count])

        print(order[count],"-->",lc[count])
        count = count + 1
        
        
    pos = lc.index(maxi(lc))
    print(order[pos],"wins\n")
    count = count + 1
    return pos,exiting

def quit(i): # to check whether the user want to quit or not 
    if i == "":
        return False
    if i.upper() == "Q":
        return True
    else:
        return False
        
#========================================================================= Main ============================================================================================================================================================

seq = ['C2','C3','C4','C5','C6','C7','C8',                              # it is the actual sequence of pririty of all card , and by this lis t we will 
       'C9','C10','CJ','CQ','CK','CA','D2',                             # check whether the player has put a higher or lower valued card from his deck of 13 cards
       'D3','D4','D5','D6','D7','D8','D9',
       'D10','DQ','DJ','DK','DA','H2','H3',
       'H4','H5','H6','H7','H8','H9','H10',
       'HJ','HQ','HK','HA','S2','S3','S4',
       'S5','S6','S7','S8','S9','S10','SJ',
       'SQ','SK','SA']                              

inp_name = input("Enter your name : ")

total_scores = {inp_name:0 , "bot1":0 , "bot2":0 , "bot3":0}            # it will contain the all total scores of each players

print("To exit the game press Q/q\n")

while True:

    total = read_sort()                                                 # we make a copy of the sequence list for the card distrubutions

    player1,bot1,bot2,bot3 = card_dis(total)                            # assigning the cards all players

    print(inp_name+str("'s"),"cards are : ",end = "")
    
    display (player1," ")                                               # printing all the cards of the player1
    
    order = [inp_name,"bot1","bot2","bot3"]
    r.shuffle(order)                                                    # shuffling the order of players
    order2 = {inp_name:player1,"bot1":bot1,"bot2":bot2,"bot3":bot3}     # linking the names with the actual named list

    pot_win2  = {}
    for z in range(4):      # determming the potential of each payer aand then assigning them to a dictionary pot_win2
        if "bot" in order[z]:
            pot_win2[order[z]] = pot_win(order2[order[z]])
        else:
            pot_win2[order[z]] = int(input("Enter your number of potential win "))
    
    print("\nThe sequence of the play will be",order[0],"->",order[1],"->",order[2],"->",order[3])

    
    print(order[0],"will start the game\n")

    input("Press any button to start the Card Game")
    print("Good luck",inp_name)
    print("The game is started !!!!")
    print("\n")

    turn = 1
    player1_win = 0         # for counting the 
    bot1_win = 0            # no of times each player had won
    bot2_win = 0
    bot3_win = 0
    
    while True:             # it will execute 13 times
        if turn == 14:
            break 
        print("-" * 80)
        print("Turn"+str(turn))
    
        pos,exiting = run(order,order2)
        if exiting:         # checking whether the user want to exit or not
            break
        if order[pos] == inp_name:
            player1_win += 1
        elif order[pos] == "bot1":
            bot1_win += 1
        elif order[pos] == "bot2":
            bot2_win += 1
        elif order[pos] == "bot3":
            bot3_win += 1
    
        order = collections.deque(order)
        order.rotate(-pos)  # based on the position of winner we shift his turn to the begining/ at the first pos of order list 
        order = list(order)
        print("-" * 80)
        print("Next order will be",end = " ")
        display(order," -> ")
        turn = turn + 1
        input("Press Enter to continue ! ")
        print("\n"*2)

    order3 = {inp_name:player1_win,"bot1":bot1_win,"bot2":bot2_win,"bot3":bot3_win} # for linking the player names with their total no of win
    print("Scores are as follows : ")
    scores = []
    print("\n The scores of this round are : ")
    for z in order:
        x = pot_win2[z]
        y = order3[z]
        if x > y:
            print(z,"= -10 *",x,"( y = ",y,", x =",x,")")
            scores.append(-10*x)
            total_scores[z] += -10*x  
        else:
            print(z,"= 10 *",x,"+(",y,"-",x,"),(y =" ,y,", x =",x,")")
            scores.append(10*x + (y-x))
            total_scores[z] += 10*x + (y-x)

    pos2 = scores.index(max(scores))
    count2 = scores.count(max(scores)) # counting how many have the max scores

    if count2 > 1:                     # to check whether the match is draw or not
        print("Match is draw !!!")
    else:
        print()
        print(order[pos2],"is the winner !!!!! ")

    if exiting: # if the user want to exit the game between the match 
        print("\nYou qiut the match :( ")
        print("Final Scores are")
        for z in order:
            print(z,"=",total_scores[z])
        break
    
    inp4 = input("Continue (Y/N) ")
    if inp4 == "Y":
        continue
    else:
        for z in order:
            print(z,"=",total_scores[z])
        break

print("\nTHE END :)\n")
print(40*"=-")
#================================================================================ The End ============================================================================================================
