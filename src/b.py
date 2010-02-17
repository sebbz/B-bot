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
        
    def getPlayers(self):
        players = []
        for player in self.players:
            players.append(str(player))
        return 
        
    def startGame(self):
        pass
    
    def placeSequence(self, player, cards):
        self.players.index(player).placeSequence(cards)
        
    def showPlayersPlacedCards(self, player):
        return self.players.index(player).getPlacedCards()
    
    def drawFromDeck(self, player):
        if len(self.deck) > 0:
            self.players.index(player).giveCards(self.deck.pop())
            return True
        else:
            return False
    
    def putCardBackInDeck(self, card):
        self.deck.append(card)
    
    def drawFromPlayer(self, nasty_player, victim_player):
        victim_cards = self.players.index(victim_player).getHeldCards()
        stolen_card = victim_cards.shuffle().pop()
        self.players.index(victim_player).removeCard(stolen_card)
        self.players.index(nasty_player).giveCards([stolen_card])
    
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
    
    def getHeldCards(self):
        return list(self.held_cards)
    
    def getPlacedCards(self):
        return list(self.placedCards)
    
    def removeCard(self, card):
        if card in self.held_cards:
            self.held_cards.remove(card)
            return True
        return False
    
    def placeSequence(self, cards):
        self.placedCards |= cards
        self.held_cards -= cards
    
    def __str__(self):
        return self.name   
    