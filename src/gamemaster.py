# coding=utf-8
import time
import b
import bbot

class GameMaster:
    def __init__(self, bbot):
        self.playing = False
        self.bbot = bbot
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
        return "fuck OFF %s!!!!!!!" % nick.upper()

    def newGame(self, nick):
        if self.playing:
            return "A game is already in progress..."
        self.b = b.B(nick)
        self.b.addPlayer(nick)
        self.playing = True
        return "A new game has been created by %s. Type b.join to join in" % nick

    def join(self, nick):
        str = "Couldn't add %s. Players: %s " % (nick, " ".join(self.b.getPlayers()))
        if self.b.addPlayer(nick):
            str = "%s joined! Players: " % nick
            str += " ".join(self.b.getPlayers())
        return str

    def startGame(self, nick):
        if not self.playing:
            return "No game to start"
        if self.b.getStartPlayer() != nick:
            return "Only %s can start the game" % self.b.getStartPlayer()
        if len(self.b.getPlayers()) < 2:
            return "You need more players!!!"
        self.bbot.sendChanMsg("Deck has been sorted")
        self.bbot.sendPrivMsg("grul", "HEJ!!!!!!!!!")
        self.b.shuffleDeck()
