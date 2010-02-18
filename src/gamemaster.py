# coding=utf-8
import time
import b
import bbot

class GameMaster:
    def __init__(self, bbot):
        self.playing = False
        self.has_game = False
        self.bbot = bbot
        self.current_player = ""
    def handleMessage(self, nick, msg):
        msg = msg.strip()
        if msg == "new game":
            return self.newGame(nick)
        if msg == "start game":
            return self.startGame(nick)
        if msg == "help":
            pass
        if msg == "draw":
            return self.draw(nick)
        if msg == "join":
            return self.join(nick)
        if msg == "done":
            return self.done(nick)
        return "Fuck OFF %s!!!!!!!" % nick.upper()

    def newGame(self, nick):
        if self.has_game:
            return "A game is already in progress..."
        self.b = b.B(nick)
        self.b.addPlayer(nick)
        self.has_game = True
        return "A new game has been created by %s. Type b.join to join in" % nick

    def join(self, nick):
        str = "Couldn't add %s. Invalid game!" % nick
        if (self.has_game and not self.playing):
            if self.b.addPlayer(nick):
                str = "%s joined! Players: " % nick
                str += " ".join(self.b.getPlayers())
        return str

    def startGame(self, nick):
        if not self.has_game:
            return "No game to start"
        if self.playing:
            return "Game has already started"
        if self.b.getStartPlayer() != nick:
            return "Only %s can start the game" % self.b.getStartPlayer()
        if len(self.b.getPlayers()) < 2:
            return "You need more players!!!"
        self.playing = True
        self.bbot.sendChanMsg("Deck has been sorted")
        self.b.shuffleDeck()
        self.bbot.sendChanMsg("Dealing cards")
        self.b.dealCards()
        for player in self.b.getPlayers():
            self.__sendPlayersCards(player)
        self.current_player = self.b.getRandomPlayer()
        return "Game started! %s's turn" % self.current_player

    def draw(self, nick):
        if not self.playing:
            return "No game started, CANNOT dRAW YOU DUMBFUCK %s" % nick
        if self.current_player == nick:
            if self.b.drawFromDeck(nick):
                self.__sendPlayersCards(nick)
                return "%s drew a card, do something else or b.done" % (nick)
            return "ERON"
        else:
            return "IT IS NOT YOUR TURN %s STOOPOD!?" % nick
    
    def done(self, nick):
        if not self.playing:
            return "No game started, CANNOT LOL YOU DUMBFUCK %s" % nick
        if self.current_player == nick:
            self.current_player = self.b.getNextPlayer()
            return "%s done, %s's turn" % (nick, self.current_player)
        else:
            return "not %s turn"  % nick

    def __sendPlayersCards(self, nick):
        text = "Your cards: "
        for card in self.b.getPlayerCards(nick):
            text += str(card)
            text += " "
        self.bbot.sendPrivMsg(nick, self.__replaceSuitCards(text))

    def __replaceSuitCards(self, cards):
        """ cards is a string with cards 2-14 whatever
        """
        return cards.replace("11", "B").replace("12", "Q").replace("13", "K").replace("14", "A")
