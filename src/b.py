'''
@author: WICKEDNETS OF DOAAAAAM
'''

class B(object):
    """
    HAPPY B CLASS FOR EXTREME GAMING SENSATION!!!!
    """

    def __init__(self):
        self.players = []
        self.deck = range(2,14)
    
    def addPlayer(self, player_name):
        self.players.append(Player(player_name))
        
    def startGame(self):
        pass
    
    def placeSequence(self, player, cards):
        pass 
        
    def showPlayersTableCards(self, player):
        pass
    
    def drawFromDeck(self, player):
        player.giveCards(self.deck.pop())
    
    def drawFromPlayer(self, nasty_player, victim_player):
        pass
    
    def shuffleDeck(self):
        self.deck.shuffle()
    
    def dealCards(self):
        for player in self.players:
            player.giveCards([self.deck.pop(), self.deck.pop()])
    
class Player():
    """
    This is a player. He likes women with small feet though all other women seem to take much interest in him. The player usually plays along and entertain the women, thence a player.
    """
    def __init__(self, name):
        self.name = name
        self.held_cards = set()
        self.placedCards = set()
    
    def giveCards(self, cards):
        self.held_cards |= cards
    
    def heldCards(self):
        return self.held_cards
    
    def removeCard(self, card):
        if card in self.held_cards:
            self.held_cards.remove(card)
            return True
        return False
    
    def placeSequence(self, cards):
        self.placedCards |= cards
        self.held_cards -= cards
        
        