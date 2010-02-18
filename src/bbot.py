# coding=utf-8
import sys
import socket
import signal

import gamemaster

def signal_handler(signal, frame):
    global b
    del(b)

class BBot:
    def __del__(self):
        self.s.close()
        print "TERMINATING"

    def __init__(self):
        self.buffer = ""
        self.HOST = "irc.se.quakenet.org"
        self.PORT = 6667
        self.NICK = "TALKSHOWHOST"
        self.IDENT = "b-boten"
        self.REALNAME ="b botson"
        self.OWNER = "grul" # lol, ägd robot
        self.CHANNEL = "#b-game"

        self.s = socket.socket()
        print "Connecting..."
        self.s.connect((self.HOST, self.PORT))
        print "Sending NICK..."
        self.s.send("NICK %s\r\n" % self.NICK)
        print "Sending USER..."
        self.s.send("USER %s %s %s :%s\r\n" % (self.IDENT, self.IDENT, self.IDENT, self.REALNAME))

        self.pings = 0

        self.gm = gamemaster.GameMaster(self)

        print "Main loop..."
        while True:
            self.buffer += self.s.recv(2048)
            lines = self.buffer.split("\n")
            self.buffer = lines.pop()
            for line in lines:
                print line
                if line.find("PING") != -1:
                    self.pings += 1
                    self.s.send("PONG %s\r\n" % line.split()[1])
                    if self.pings == 2:
                        self.s.send("JOIN %s\r\n" % self.CHANNEL)
                if line.find("PRIVMSG") != -1:
                    print line
                    nick = line.split()[0].split(":")[1].split("!")[0]
                    print "nick: %s" % nick
                    message = line.split(" ", 3)[3][1:]
                    print "message: %s" % message

                    if message.startswith("b."):
                        l = self.gm.handleMessage(nick, message[2:])
                        if l != "":
                            self.s.send("PRIVMSG %s :%s\r\n" % (self.CHANNEL, l))
    def sendPrivMsg(self, nick, msg):
        self.s.send("PRIVMSG %s :%s\r\n" % (nick, msg))

    def sendChanMsg(self, msg):
        self.s.send("PRIVMSG %s :%s\r\n" % (self.CHANNEL, msg))

if __name__ == "__main__":
    b = BBot()
    signal.signal(signal.SIGINT, signal_handler)
