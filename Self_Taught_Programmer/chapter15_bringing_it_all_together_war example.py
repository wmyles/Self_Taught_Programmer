#war

from random import shuffle
class Card:
    #class so we can share the variables across objcts in class
    suits=["spades",
           "hearts",
           "diamonds",
           "clubs"]
    values=[None,None,"2","3",
            "4","5","6","7","8","9","10","Jack",# you need class variables because in the repr method we use the instance variables as indexes for the class variable, smart!
            "Queen","King","Ace"] # matching index, fil first two with none so val[2]=2  so index matches card value (2,1) would be 2 of hearts
    def __init__(self,v,s):
        self.value=v
        self.suit=s
        """suit+value are ints"""
    def __lt__(self,c2):#defining magic method for less than(if objects are operands you need magic method)
        if self.value<c2.value:
            return True # check value of two cads
        if self.value==c2.value:
            if self.suit<c2.suit: #suite will be tiebreaker!
                return True
        else:
            return False # then its not less than
        return False
    def __gt__(self, c2): # need to do this for each operand < and > than 
        if self.value>c2.value:
            return True
        if self.value==c2.value:
            if self.suit>c2.suit:
                return True
        else:
            return False# if the two above are wrong than this card is  not greater than
        return False
    def __repr__(self):
        v=self.values[self.value]+" of "\ # i think the class variables are only needed so we can print the cards object, they arent used in the comparisons
           +self.suits[self.suit] # this magic method normally tells us where object is when you print object but we are overriding it so when we print the object we get what we want
        return v
class Deck:# visualize deck being separate from the cards above
    def __init__(self):
        self.cards=[]
        for i in range (2,15): #cards in a suit
            for j in range(4): #suits (club,spades,heart diamonds) rememer comps start at 0
                self.cards.append(Card(i,j))# append the newly created card to the self.card list and go through loop again to create a list 
        shuffle(self.cards)
    def rm_card(self): #remaining cards
        if len(self.cards)==0: #length counds numbr of indices
            return
        return self.cards.pop()
class Player:
    def __init__(self,name):
        self.wins=0
        self.card=None
        self.name=name
        #review the game section
class Game:
    def __init__(self):
        name1=input(" p1 name ")
        name2=input(" p2 name")
        self.deck=Deck()# class deck?
        self.p1=Player(name1)
        self.p2=Player(name2)

    def wins(self, winner):
        w = "{} wins this round"
        w=w.format(winner)
        print(w)
    def draw(self, p1n, p1c, p2n, p2c): #drawing of player 1 and player2's cards from desk and the names of player
        d="{} drew {} {} drew {}"
        d=d.format(p1n,p1c,p2n,p2c)
        print(d)
    def play_game(self):
        cards=self.deck.cards
        print("beginning War!")
        while len(cards) >= 2:
            m="q to quite. Any" + "key to play:"
            response=input(m) # storing the prompt in a variable and passing it to input then storing the user input
            if response=='q':
                break
            p1c=self.deck.rm_card()
            p2c=self.deck.rm_card()
            p1n=self.p1.name
            p2n=self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c>p2c:
                self.p1.wins+=1
                self.wins(self.p1.name)
            else:
                self.p2.wins +=1
                self.wins(self.p1.name)

            win=self.winner(self.p1, self.p2)
            print("war is over. {} wins".format(win))
    def winner(self, p1,p2):
        if p1.wins>p2.wins:
            return p1.name
        if p1.wins <p2.wins:
            return p2.name
        return "it was a tie!"
game=Game()
game.play_game()

    
    
        
    
    
