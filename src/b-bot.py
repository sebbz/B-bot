# coding=utf-8
import sys
import socket
import signal

import gamemaster

def terminate():
    global s
    print """
############
TERMINATING
############"""
    s.close()
    sys.exit()

def signal_handler(signal, frame):
    terminate()

signal.signal(signal.SIGINT, signal_handler)

buffer = ""

HOST="irc.se.quakenet.org"
PORT=6667
NICK="TALKSHOWHOST"
IDENT="b-boten"
REALNAME="b botson"
OWNER="grul"
CHANNEL="#b-game"

s=socket.socket()
print "Connecting..."
s.connect((HOST, PORT))
print "Sending NICK..."
s.send("NICK %s\r\n" % NICK)
print "Sending USER..."
s.send("USER %s %s %s :%s\r\n" % (IDENT, IDENT, IDENT, REALNAME))

pings = 0

gm = gamemaster.GameMaster()

print "Main loop..."
while True:
    buffer += s.recv(2048)
    lines = buffer.split("\n")
    buffer = lines.pop()
    for line in lines:
        print line
        if line.find("PING") != -1:
            pings += 1
            s.send("PONG %s\r\n" % line.split()[1])
            if pings == 2:
                s.send("JOIN %s\r\n" % CHANNEL)
        if line.find("PRIVMSG") != -1:
            print line
            nick = line.split()[0].split(":")[1].split("!")[0]
            print "nick: %s" % nick
            message = line.split(" ", 3)[3][1:]
            print "message: %s" % message

            if message.startswith("b."):
                l = gm.handlemessage(message[2:])
                if l != "":
                    s.send("PRIVMSG %s :%s\r\n" % (CHANNEL, l))

