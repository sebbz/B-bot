'''
@author: WICKEDNETS OF DOAAAAAM
'''

import random

class B(object):
    """
    HAPPY B CLASS FOR EXTREME GAMING SENSATION!!!!
    """

    def __init__(self, start_player):
        self.players = []
        self.deck = range(2,15)
        self.start_player = start_player
    
    def addPlayer(self, player_name):
        if len(self.players) > 3:
            return False
        for p in self.players:
            if p.name == player_name:
                return False
        self.players.append(Player(player_name))
        return True
        
    def getPlayers(self):
        players = []
        for p in self.players:
            players.append(str(p))
        return players
        
    def getStartPlayer(self):
        return self.start_player
    
    def startGame(self, player):
        """ IS THIS EVEN SUPPOSED TO BE HERE!?! haha I'll leave it! :D
        """
        if self.start_player is not player:
            return False
        return True
    
    def placeSequence(self, player, cards):
        for p in self.players:
            if p.name == player:
                if p.placeSequence(cards):
                    return True
        return False
        
    def showPlayersPlacedCards(self, player):
        for p in self.players:
            if p.name == player:
                return p.getPlacedCards()
        return None
    
    def drawFromDeck(self, player):
        if len(self.deck) > 0:
            for p in self.players:
                if p.name == player:
                    p.giveCards(set([self.deck.pop()]))
            return True
        else:
            return False
    
    def putPlayerCardBackInDeck(self, player, card):
        for p in self.players:
            if p.name == player:
                p.removeCard(card)
        self.deck.append(card)
    
    def drawFromPlayer(self, nasty_player, victim_player):
        for p in self.players:
            if p.name == nasty_player:
                np = p
            if p.name == victim_player:
                vp = p
        victim_cards = vp.getHeldCards()
        stolen_card = random.choice(victim_cards)
        vp.removeCard(stolen_card)
        np.giveCards(set([stolen_card]))
        return stolen_card
    
    def shuffleDeck(self):
        temp_deck = []
        while self.deck:
            card = random.choice(self.deck)
            self.deck.remove(card)
            temp_deck.append(card)
        self.deck = temp_deck
    
    def dealCards(self):
        for player in self.players:
            player.giveCards(set([self.deck.pop(), self.deck.pop()]))
            
    def getPlayerCards(self, player):
        for p in self.players:
            if p.name == player:
                return p.getHeldCards()
        return None
    
    def getRandomPlayer(self):
        return str(random.choice(self.players))
    
class Player():
    """
    This is a player. He likes women with small feet though all other women seem to take much interest in him. The player usually plays along and entertain the women, thence a player.
    """
    def __init__(self, name):
        self.name = name
        self.held_cards = set()
        self.placed_cards = set()
    
    def giveCards(self, cards):
        self.held_cards |= cards
    
    def getHeldCards(self):
        return list(self.held_cards)
    
    def getPlacedCards(self):
        return list(self.placed_cards)
    
    def removeCard(self, card):
        if card in self.held_cards:
            self.held_cards.remove(card)
            return True
        return False
    
    def placeSequence(self, cards):
        matched = False
        #IS THIS D?
        if 14 in cards:
            matched = self.__checkForSequence(cards)
            if not matched:
                cards.remove(14)
                cards.append(1)
                matched = self.__checkForSequence(cards)
        else:
            matched = self.__checkForSequence(cards)
        if not matched:
            return False
        cards = set(cards)
        if cards <= self.held_cards:
            self.placed_cards |= cards
            self.held_cards -= cards
            return True
        return False
    
    def __checkForSequence(self, cards):
        cards.sort()
        matched = True
        for i in range(len(cards)):
            if cards[0]+i != cards[i]:
                matched = False
        return matched

    
    def __str__(self):
        return self.name   

if __name__ == '__main__':
    #TEST CODE FOR TEST PURPOSES ONLY!! :D:D:D:
    
    game = B('hitler')
    game.addPlayer('hitler')
    game.addPlayer('adolfu')
    print game.getPlayers()
    game.shuffleDeck()
    game.dealCards()
    print 'hitler cards: ', game.getPlayerCards('hitler'), 'adolfu cards: ', game.getPlayerCards('adolfu')
    #print 'hitler draws one from deck'
    #game.drawFromDeck('hitler')
    #print 'hitler cards: ', game.getPlayerCards('hitler')
    #print 'hitler will now steal one card from adolfu:'
    #game.drawFromPlayer('hitler', 'adolfu')
    #print 'hitler cards: ', game.getPlayerCards('hitler'), 'adolfu cards: ', game.getPlayerCards('adolfu')
    #print 'hitler will now put back one card into the deck'
    #game.putPlayerCardBackInDeck('hitler', 5)
    print 'hitler cards: ', game.getPlayerCards('hitler'), 'adolfu cards: ', game.getPlayerCards('adolfu')
    print 'hitler will place some cards'
    print game.placeSequence('hitler', game.getPlayerCards('hitler'))
