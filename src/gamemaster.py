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
        self.draw_counter = 0

    def handleMessage(self, nick, msg):
        """ TODO: b.steal, b.place, mer?
        """
        msg = msg.strip()
        if msg == "new game":
            return self.newGame(nick)
        if msg == "start game":
            return self.startGame(nick)
        if msg == "help":
            return "commands: b.new game, b.join, b.start game, b.draw, b.drop, b.done" # TODO MEEEER! förklaringar kanske
        if msg == "draw":
            return self.draw(nick)
        if msg == "join":
            return self.join(nick)
        if msg == "done":
            return self.done(nick)
        if msg == "players":
            return self.getPlayers()
        if msg.startswith("drop"):
            return self.dropCard(nick, msg)
        if msg.startswith("cards"):
            if self.playing:
                self.__sendPlayersCards(nick)
                return None
            else:
                return "%s, not playing" % nick
        return "Fuck OFF %s!!!!!!!" % nick.upper()

    def newGame(self, nick):
        if self.has_game:
            return "A game is already in progress..."
        self.b = b.B(nick)
        self.b.addPlayer(nick)
        self.has_game = True
        return "A new game has been created by %s. Type b.join to join in" % nick

    def join(self, nick):
        str = "Couldn't add %s. Maybe the game is full or has already started!" % nick
        if self.has_game:
            str += " Players: %s" % ", ".join(self.b.getPlayers())
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
            """Man får bara ta ett kort om:
            två kort på handen, i början av rundan
            eller
            under två kort på handen, resten av rundan
            """
            if (self.draw_counter == 0 and len(self.b.getPlayerCards(nick)) == 2) or (self.draw_counter >0 and len(self.b.getPlayerCards(nick)) < 2):
                if self.b.drawFromDeck(nick):
                    self.__sendPlayersCards(nick)
                    self.draw_counter += 1
                    return "%s drew a card, do something else or b.done" % (nick)
                return "ERON"
            else:
                return "%s, draw not ALLAWOD" % nick
        else:
            return "IT IS NOT YOUR TURN %s STOOPOD!?" % nick

    def dropCard(self, nick, msg):
        if self.current_player != nick:
            return "%s, NOT YOUR TURN" % nick
        error_msg = "Failure! Example b.drop B"
        if len(msg) != 6:
            self.bbot.sendPrivMsg(nick, error_msg)
            return ""
        else:
            card = 0
            try:
                card = int(msg[5].lower().replace("b", "11").replace("q", "12").replace("k", "13").replace("a", "14"))
            except ValueError:
                self.bbot.sendPrivMsg(nick, error_msg)
                return ""
            cards = self.b.getPlayerCards(nick)
            if len(cards) < 3:
                self.bbot.sendPrivMsg(nick, "You don't have enough cards")
                return ""
            if not card in cards:
                self.bbot.sendPrivMsg(nick, "You don't have that card")
                return ""
            self.b.putPlayerCardBackInDeck(nick, card)
            self.__sendPlayersCards(nick)
            return "%s dropped a card" % nick

    def done(self, nick):
        """ man måste ha dratt eller slut på kort i leken för att få göra done
            och så får man inte ha fler än 2 kort på hand
            och inte färre än 2 om det finns kort att SNO. f.eks. från andra spelare
            eller från leken.
        """
        if not self.playing:
            return "No game started, CANNOT LOL YOU DUMBFUCK %s" % nick
        if self.draw_counter == 0: # lite or och sånt på det där i kommentaren ovanför
            return "%s: You have to draw a card first" % nick
        if self.current_player == nick:
            self.current_player = self.b.getNextPlayer()
            self.draw_counter = 0
            return "%s done, %s's turn" % (nick, self.current_player)
        else:
            return "not %s turn"  % nick

    def getPlayers(self):
        if self.has_game:
            return "Players: %s" % ", ".join(self.b.getPlayers())
        else:
            return "There isn't even a game, fool!"

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
