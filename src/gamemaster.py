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
            pass
        if msg == "join":
            return self.join(nick)
        return "Fuck OFF %s!!!!!!!" % nick.upper()

    def newGame(self, nick):
        if self.has_game:
            return "A game is already in progress..."
        self.b = b.B(nick)
        self.b.addPlayer(nick)
        self.has_game = True
        return "A new game has been created by %s. Type b.join to join in" % nick

    def join(self, nick):
        str = "Couldn't add %s. Players: %s " % (nick, " ".join(self.b.getPlayers()))
        if (not self.playing) and self.b.addPlayer(nick):
            str = "%s joined! Players: " % nick
            str += " ".join(self.b.getPlayers())
        return str

    def startGame(self, nick):
        if not self.has_game:
            return "No game to start"
        if not self.playing:
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
            text = "Your cards: "
            for card in self.b.getPlayerCards(player):
                text += str(card)
                text += " "
            self.bbot.sendPrivMsg(player, text)
        self.current_player = self.b.getRandomPlayer()
        return "Game started! %s's turn" % self.current_player
